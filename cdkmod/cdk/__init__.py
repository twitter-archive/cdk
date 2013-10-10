# -*- coding: utf-8 -*-
"""
cdk - course development toolkit. Convert asciidoc input to deck.js
slidedecks with many code/development oriented features.

Current features list includes:

 * single file output thanks to data:uri

Usage:
  cdk FILE

Arguments:
  FILE     asciidoc source file
Options:
  -h --help     Show this screen.

"""

import subprocess
from os.path import dirname, join, abspath

from docopt import docopt
from schema import Schema, And, Or, Use, SchemaError

"""
CDK_DIR=$( cd "$( dirname "$0" )" && pwd )
eval ${CDK_DIR}/external/asciidoc/asciidoc.py -f ${CDK_DIR}/external/asciidoc/asciidoc.conf ${attrs[@]} $@
"""


def main():
    """Entry point for stitching together our custom asciidoc conf, deckjs
    conf and plugins.

    """
    data_dir = join(abspath(dirname(__file__)),  "data")
    custom_dir = join(abspath(dirname(__file__)),  "custom")
    asciidoc_dir = join(data_dir, "asciidoc-8.6.8")
    
    
    # Setup asciidoc command we want to run
    cmd = ("%(asciidoc_dir)s/asciidoc.py -b deckjs "
           "-a deckjs_theme=twitter -a data-uri "
           "-f %(custom_dir)s/asciidoc.conf "
           "-a iconsdir='%(data_dir)s/images/icons' -a icons") % locals()
    cmd = cmd.split()
    
    
    # Try parsing command line args and flags with docopt
    arguments = docopt(__doc__, version="cdk 0.1")

    # Check for valid args and flags
    schema = Schema({'FILE': And(str, len)})
    try:
        arguments = schema.validate(arguments)
    except SchemaError as e:
        exit(e)

    # Great! Run asciidoc with appropriate flags
    cmd.append(arguments['FILE'])
    try:
        subprocess.check_output(cmd)
    except subprocess.CalledProcessError as e:
        exit(e.output)
        
    
if __name__ == '__main__':
    main()
