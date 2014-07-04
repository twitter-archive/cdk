# -*- coding: utf-8 -*-

import unittest

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
    
from .context import cdk

class BasicTestSuite(unittest.TestCase):
    """Unit tests go here!"""
    
    def test_inserting_custom_css(self):
        """Custom css means opening the produced .html and sneaking
        a style tag before the closing </body> tag."""
        
        source_fp = StringIO('<p>a bunch of</p> html</body>\r\n</html>\r\n')
        cdk.add_css_to_stream(source_fp, 'My rules')
        source_fp.seek(0)
        out = '<p>a bunch of</p> html<style type="text/css">\r\nMy rules\r\n</style>\r\n</body>\r\n</html>\r\n'
        self.assertEqual(out, source_fp.read())

    def test_toc_gets_numbered(self):
        cmd = cdk.create_command("basic", toc=True)
        cmd = " ".join(cmd)
        
        assert "-a toc -a numbered" in cmd

if __name__ == '__main__':
    unittest.main()
