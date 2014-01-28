# -*- coding: utf-8 -*-

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
    
from .context import cdk
from cdk import b64

def test_encoding():
    fp = StringIO("help")
    out = StringIO()
    b64.main(out, "filename.txt", fp)
    out.seek(0)
    assert out.read() == '"data:text/plain;base64,aGVscA=="'
    
