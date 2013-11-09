from __future__ import print_function

import sys
import base64
from os.path import splitext

def encode(names):
    for name in names:
        basename, ext = splitext(name)
        ext = ext.lstrip('.')
        with open(name) as fp:
            data = fp.read(32000); # max-size in data-uri I think
        b64string = base64.b64encode(data)
        template = """@{name}: "data:image/{type};base64,{data}";"""
        print(template.format(name=basename, type=ext, data=b64string))

if __name__ == '__main__':
    encode(sys.argv[1:])
