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

data_dir = join(abspath(dirname(__file__)),  "data")
asciidoc_dir = join(data_dir, "asciidoc-8.6.8")

def main():
    """Entry point for stitching together our custom asciidoc conf, deckjs
    conf and plugins.

    """
    
    # Setup asciidoc command we want to run
    cmd = ("%s/asciidoc.py -b deckjs -a deckjs_theme=twitter -a data-uri "
           "-a iconsdir='%s/images/icons' -a iconss") % (asciidoc_dir, data_dir)
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
