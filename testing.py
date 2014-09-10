#! usr/bin/env python

import unittest

class CssToSassConverter(unittest.TestCase):
    all_css_code = '''.foo .bar p {
    list-style-type: none;
    color: white;
    background: black;
}
.foo .bar p {
    text-decoration: none;
}
.foo h1 {
color: red;
}'''
    selectors_list = ['.foo .bar p', '.foo .bar p', '.foo h1']
    def test_get_selectors (self, all_css_code):
        self.assertEquals(1, 1)#self.selectors_list)

if __name__ == "__main__":
    unittest.main()