import re
import string
"""TODO;
    check todos from the original project
    more tests
"""

class CssToSassConverter:

    default_options = {
        'css_file' : 'data/main.css',
        'sass_file' : 'data/main.scss'
    }

    def __init__(self, **kwargs):
        self.options = dict(CssToSassConverter.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        'check a converter option'
        return self.options[key]

    def write_results_to_file(self):
        inname = self.options['css_file']
        outname = self.options['sass_file']

        with open(inname) as infile:
            with open(outname, "w") as outfile:
                outfile.write(self.convert(infile.read()))

    def __get_n_tabs(self, n):
        'prints the n amount of tabs for proper indentation'
        tabs = ''
        for n in range(n, 0, -1):
            tabs = tabs + '    '.ljust(n)
        return tabs

    def __get_css_for_this_selector(self, statement_blocks, selector_string):
        selector_string = selector_string.strip(' \t\n\r')
        css = ''
        for block in statement_blocks:
            regex_pattern = re.compile(r"\s*([^{]*)\s*\{([^}]*)", re.I | re.M)
            found = regex_pattern.search(block)
            found_selector = found.group(1).strip(' \t\n\r')

            if selector_string == found_selector:
                # in case we have multiple blocks applying to the same selector, add found css to our css value
                css = css + found.group(2).replace(' ', '')
                css = css.strip(' \t\n\r')
        return css

    def __convert_selectors_to_nested_dict(self, selectors):
        'converts a list of selectors to a nested dictionary'
        selectors_nested_dict = {}
        selectors_nested_list = []

        # populate the nested list of selectors
        for selector in selectors:
            selectorChunks = string.split(selector, " ")
            selectors_nested_list.append(selectorChunks)

        # populate the nested dictionary
        for path in selectors_nested_list:
            current_level = selectors_nested_dict
            for chunk in path:
                if chunk not in current_level:
                    current_level[chunk] = {}
                current_level = current_level[chunk]

        return selectors_nested_dict

    def get_statement_blocks (self, all_css_code):
        regex = re.compile(r"([0-9a-zA-Z#: \.\-_]+\{([^}]*)\})", re.I | re.M);

        # list comprehension
        statement_blocks = [match.group(1) for match in regex.finditer(all_css_code)]

        return statement_blocks

    def get_selectors (self, all_css_code):

        regex = re.compile(r"([0-9a-zA-Z#: \.\-_]+){([^}]*)\}", re.I | re.M);

        # generator selectors
        selectors = (match.group(1).strip(' \t\n\r') for match in regex.finditer(all_css_code))

        selectors_dict = self.__convert_selectors_to_nested_dict(selectors)

        return selectors_dict

    def __build_sass(self, selectors, statement_blocks, SASS = '', original_selector_string = '', level = 0):

        for parent, children in selectors.items():
            selector_string = original_selector_string + ' ' + parent

            SASS = SASS + "\n" + self.__get_n_tabs(level) + parent + " {\n"
            css = self.__get_css_for_this_selector(statement_blocks, selector_string)
            if (len(css) > 0):
                'in css replace \n for \n and appropriate amount of tabs'
                css = self.__get_n_tabs(level+1) + css.replace("\n", "\n" + self.__get_n_tabs(level+1))
            SASS = SASS + css

            if (len(children) > 0):
                SASS = self.__build_sass(children, statement_blocks, SASS, selector_string, (level + 1))

                SASS = SASS + "\n" + self.__get_n_tabs(level) + "}"
            else:
                SASS = SASS + "\n" + self.__get_n_tabs(level)+ "}"

        return SASS

    def convert (self, css):
        'the main function to convert'

        # nested dictionary of selectors
        selectors = self.get_selectors(css)
        statementBlocks = self.get_statement_blocks(css)
        SASS = self.__build_sass(selectors, statementBlocks)

        return SASS