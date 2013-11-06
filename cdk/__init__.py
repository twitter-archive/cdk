# -*- coding: utf-8 -*-
"""
cdk - course development toolkit. Convert asciidoc input to deck.js
slidedecks with many code/development oriented features.

Current features list includes:

 * single file output thanks to data:uri

Usage:
  cdk [-vb] FILE
  cdk --theme=<theme> FILE
  cdk --install-theme=<theme>
  cdk --default-theme=<theme>

Arguments:
  FILE     asciidoc source file

Options:
  --install-theme <theme>      http path to zipfile containing theme. Will be unzipped in
                               theme directory.
  --default-theme <theme>      Theme to be the default used theme when creating slide decks
  --theme <theme>              Theme to be used to create slide deck
  -v --verbose                 Verbose output from underlying commands
  -b --bare                    Simple html output, no slideshow.
  -h --help                    Show this screen.

"""

import subprocess
import zipfile
from os.path import dirname, basename, join, abspath, isfile, isdir, expanduser
from os import mkdir, unlink, listdir
from shutil import copy
import ConfigParser as cp

from docopt import docopt

LOCATION = abspath(dirname(__file__))
PREFS_DIR = expanduser("~/.cdk")
PREFS_FILE = join(PREFS_DIR, "prefs")
THEMES_DIR = join(LOCATION, "custom", "deck.js", "themes")


def set_default_theme(theme):
    """
    Set default theme name based in config file.
    """
    pref_init()  # make sure config files exist
    parser = cp.ConfigParser()
    parser.read(PREFS_FILE)
    # Do we need to create a section?
    if not parser.has_section("theme"):
        parser.add_section("theme")
    parser.set("theme", "default", theme)
    # best way to make sure no file truncation?
    with open("%s.2" % PREFS_FILE, "w") as fp:
        parser.write(fp)
    copy("%s.2" % PREFS_FILE, PREFS_FILE)
    unlink("%s.2" % PREFS_FILE,)


def pick_theme(manual):
    """
    Return theme name based on manual input, prefs file, or default to "plain".
    """
    if manual:
        return manual
    pref_init()
    parser = cp.ConfigParser()
    parser.read(PREFS_FILE)
    try:
        theme = parser.get("theme", "default")
    except (cp.NoSectionError, cp.NoOptionError):
        theme = "plain"
    return theme


def pref_init():
    """Can be called without penalty. Create ~/.cdk dir if it doesn't
    exist. Copy the default pref file if it doesn't exist."""

    # make sure we have a ~/.cdk dir
    if not isdir(PREFS_DIR):
        mkdir(PREFS_DIR)
    # make sure we have a default prefs file
    if not isfile(PREFS_FILE):
        copy(join(LOCATION, "custom", "prefs"), PREFS_DIR)


def install_theme(path_to_theme):
    """
    Pass a path to a theme file which will be extracted to the themes directory.
    """
    pref_init()
    # cp the file
    filename = basename(path_to_theme)
    dest = join(THEMES_DIR, filename)
    copy(path_to_theme, dest)
    # unzip
    zf = zipfile.ZipFile(dest)
    # should make sure zipfile contains only themename folder which doesn't conflict
    # with existing themename. Or some kind of sanity check
    zf.extractall(THEMES_DIR)  # plus this is a potential security flaw pre 2.7.4
    # remove the copied zipfile
    unlink(dest)


def create_command(theme, bare=False, filters_list=None):
    # default filters
    if not filters_list:
        filters_list = ["source/source-highlight-filter.conf",
                        "graphviz/graphviz-filter.conf"]
    # vars for locations
    DATA_DIR = join(LOCATION,  "data")
    CUSTOM_DIR = join(LOCATION,  "custom")
    ASCIIDOC_DIR = join(DATA_DIR, "asciidoc-8.6.8")

    # Setup asciidoc command we want to run with backend
    if bare:
        backend = "--conf-file=%(ASCIIDOC_DIR)s/html5.conf "
    else:
        backend = "--conf-file=%(CUSTOM_DIR)s/deckjs.conf "

    filters = ["--conf-file=%(ASCIIDOC_DIR)s/filters/{}".format(f)
               for f in filters_list]
    filters = " ".join(filters)

    cmd = " ".join(["python %(ASCIIDOC_DIR)s/asciidoc.py",
                    "--no-conf --conf-file=%(CUSTOM_DIR)s/asciidoc.conf",
                    backend,
                    filters,
                    "-b deckjs",
                    "-a deckjs_theme=%(theme)s -a data-uri",
                    "-a backend-confdir=%(CUSTOM_DIR)s",
                    "-a iconsdir=%(DATA_DIR)s/asciidoc-8.6.8/images/icons -a icons"]) % locals()
    return cmd.split()


def run_command(cmd, args):
    if args['--verbose']:
        cmd.append('-v')
        print "\n".join(cmd) + args['FILE']

    cmd.append(args['FILE'])
    try:
        print subprocess.check_output(cmd)
    except subprocess.CalledProcessError as e:
        exit(e.output)


def main():
    """Entry point for choosing what subcommand to run.
    """

    # Try parsing command line args and flags with docopt
    args = docopt(__doc__, version="cdk 0.1")
    # Am I going to need validation? No Schema for the moment...
    if args['FILE']:
        # Great! Run asciidoc with appropriate flags
        theme = pick_theme(args['--theme'])
        if theme not in listdir(THEMES_DIR):
            exit('Selected theme "%s" not found. Check ~/.cdk/prefs' % theme)
        cmd = create_command(theme, args['--bare'])
        run_command(cmd, args)
    # other commands
    elif args['--install-theme']:
        path = args['--install-theme']
        if not isfile(path):
            exit("Theme file not found.")
        if not path.endswith(".zip"):
            exit("Theme installation currently only supports theme install from "
                 ".zip files.")
        install_theme(path)
    elif args['--default-theme']:
        set_default_theme(args['--default-theme'])

if __name__ == '__main__':
    main()
