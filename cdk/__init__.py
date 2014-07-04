# -*- coding: utf-8 -*-
"""cdk - course development toolkit. Convert asciidoc input to deck.js slidedecks with many
code/development oriented features.

Usage:
  cdk [-vbo] [--toc] [--notransition] [--logo=<logo>] [--theme=<theme>] [--custom-css=<cssfile>] FILE
  cdk --install-theme=<theme>
  cdk --default-theme=<theme>
  cdk --generate=<name>

Arguments:
  FILE     asciidoc source file

Options:
  --install-theme <theme>      http path to zipfile containing theme. Will be unzipped in
                               theme directory.
  --default-theme <theme>      Theme to be the default used theme when creating slide decks
  --theme <theme>              Theme to be used to create slide deck
  --logo <logo>                Logo file to be used in theme. Logo should be ~200x200px image.
                               Guaranteed support only in "plain" theme.
  --custom-css <cssfile>       Additional style rules to be added to the slide deck. You'll be
                               responsible for packing any external resources (images, fonts, etc).
  --generate <name>            Generate sample slide source in file name. Try "slides.asc"
  -v --verbose                 Verbose output from underlying commands
  -b --bare                    Simple html output, no slideshow.
  -o --open                    Open the compiled slide presentation automatically
  --toc                        Add Table of Contents to output. Typically used with -b. When used
                               on normal slide deck adds section numbers to pop-up TOC.
  --notransition               Don't use transitions between slides.
  -h --help                    Show this screen.

"""

from __future__ import print_function

import subprocess
import webbrowser
import zipfile
from os.path import (dirname, basename, join, abspath, isfile, isdir,
                     expanduser, splitext)
from os import mkdir, unlink, listdir
from shutil import copy

# Python version compat checks/fixes
try:
    import ConfigParser as cp  # Python 2
except ImportError:
    import configparser as cp  # Python 3

try:
    subprocess.check_output
except AttributeError:
    import to6
    subprocess.check_output = to6.check_output

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


def create_command(theme, bare=False, toc=False, notransition=False, logo=None, filters_list=None):
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
        backend = "--conf-file=%(CUSTOM_DIR)s/html5.conf "
    else:
        backend = "--conf-file=%(CUSTOM_DIR)s/deckjs.conf "

    toc_directive = ''
    if toc:
        toc_directive = '-a toc -a numbered'
    transition = ''
    if notransition:
        transition = '-a notransition'
    logo_directive = ''
    if logo:
        logo_directive = '-a logo=%(logo)s'
    filters = ["--conf-file=%(ASCIIDOC_DIR)s/filters/{0}".format(f) for f in filters_list]
    filters = " ".join(filters)

    cmd = " ".join(["python %(ASCIIDOC_DIR)s/asciidoc.py",
                    "--no-conf --conf-file=%(CUSTOM_DIR)s/asciidoc.conf",
                    backend,
                    filters,
                    transition,
                    "-b deckjs",
                    "-a deckjs_theme=%(theme)s -a data-uri",
                    "-a backend-confdir=%(CUSTOM_DIR)s",
                    logo_directive,
                    toc_directive,
                    "-a iconsdir=%(DATA_DIR)s/asciidoc-8.6.8/images/icons -a icons"]) % locals()
    return cmd.split()


def run_command(cmd, args):
    if args['--verbose']:
        cmd.append('-v')
        print("\n".join(cmd) + args['FILE'])

    cmd.append(args['FILE'])
    try:
        print(subprocess.check_output(cmd))
    except subprocess.CalledProcessError as e:
        exit(e.output)


# Low-level functionality, exposed for easier testing.
def add_css_to_stream(out, css):
    # Seek to the end the file
    out.read(-1)
    end = "</body>\r\n</html>\r\n"
    out.seek(out.tell() - len(end))
    # Ok, now write a style tag
    out.write('<style type="text/css">\r\n')
    out.write(css)
    out.write("\r\n</style>\r\n" + end)

def add_css(out_file, css):
    with open(out_file, "r+") as out:
        add_css_to_stream(out, css)

def add_css_file(out, css_file):
    with open(css_file) as css_fp:
        add_css(out, css_fp.read())


def output_file(source_file):
    basename, ext = splitext(source_file)
    return basename + ".html"


def main():
    """
    Entry point for choosing what subcommand to run. Really should be using asciidocapi
    """
    # Try parsing command line args and flags with docopt
    args = docopt(__doc__, version="cdk")
    # Am I going to need validation? No Schema for the moment...
    if args['FILE']:
        out = output_file(args['FILE'])
        # Great! Run asciidoc with appropriate flags
        theme = pick_theme(args['--theme'])
        if theme not in listdir(THEMES_DIR):
            exit('Selected theme "%s" not found. Check ~/.cdk/prefs' % theme)
        cmd = create_command(theme, args['--bare'], args['--toc'], args['--notransition'],
                             args['--logo'])
        run_command(cmd, args)
        if args['--toc']:
            add_css(out, '.deck-container .deck-toc li a span{color: #888;display:inline;}')
        if args['--custom-css']:
            add_css_file(out, args['--custom-css'])
        if args['--open']:
            webbrowser.open("file://" + abspath(out))

    # other commands
    elif args['--generate']:
        if isfile(args['--generate']):
            exit("%s already exists!" % args['--generate'])
        with open(args['--generate'], "w") as fp:
            sample = join(LOCATION,  "custom", "sample.asc")
            fp.write(open(sample).read())
            print("Created sample slide deck in %s..." % args['--generate'])
        exit()

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
