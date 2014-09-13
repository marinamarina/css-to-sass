import unittest
from converter.convert import CssToSassConverter

class TestCssToSassConverter(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.converter = CssToSassConverter()

        # raw test data
        self.test_data = '''.foo .bar p {
            list-style-type: none;
            color: #505050;
            background: black;
        }
        .foo .bar p {
            color: black;
        }
        .foo .bar {
            text-decoration: none;
        }
        .foo h1 {
            color: red;
        }'''

        # main css converted into a list of blocks of css
        self.statement_blocks = ['''.foo .bar p {
            margin-bottom: 1em;
            color: #505050;
            background: black;
        }''',
        '''.foo .bar p {
            padding: 0;
        }''',
        '''.foo .bar {
            text-decoration: none;
        }''',
        '''.foo h1 {
            color: red;
        }''']

        # test list of selectors
        self.selectors_list = ['.foo .bar', '.foo .bar p', '.foo h1']

        self.selectors_nested_dictionary =  {'.foo': {'h1': {}, '.bar': {'p': {}}}}


    def test_get_n_tabs (self):
        self.assertEquals(self.converter._CssToSassConverter__get_n_tabs(1), '    ', "get_n_tabs did not return 1 tab")
        self.assertEquals(self.converter._CssToSassConverter__get_n_tabs(2), '        ', "get_n_tabs did not return 2 tabs")

    def test_get_css_for_this_selector(self):
        self.assertEquals(self.converter._CssToSassConverter__get_css_for_this_selector(self.statement_blocks, self.selectors_list[0]), 'text-decoration:none;')

        # test multiple occurrences of the selector in css, '.foo .bar p' repeats two times
        self.assertEquals(self.converter._CssToSassConverter__get_css_for_this_selector(self.statement_blocks, self.selectors_list[1]), 'margin-bottom:1em;\ncolor:#505050;\nbackground:black;\npadding:0;')

    def test_convert_selectors_to_nested_dict(self):
        self.assertEquals(self.converter._CssToSassConverter__convert_selectors_to_nested_dict(self.selectors_list), self.selectors_nested_dictionary)

    def test_get_selectors (self):
        self.assertEquals(self.converter.get_selectors(self.test_data), self.selectors_nested_dictionary)

    def test_get_statement_blocks (self):
        pass
        #self.assertEquals(self.converter.get_statement_blocks(self.test_data), self.statement_blocks)


if __name__ == "__main__":
    unittest.main()