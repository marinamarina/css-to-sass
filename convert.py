# !/usr/bin/env python

import re
import string

class CssToSassConverter:

    # HELPER
    def __get_n_tabs(self, n):
        'prints the n amount of tabs'
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

    def convert (self, css):
        'the main function to convert'

        # nested dictionary of selectors
        selectors = self.get_selectors(css)
        statementBlocks = self.get_statement_blocks(css)
        SASS = self.__build_sass(selectors, statementBlocks)

        return SASS

    # Level 1
    def __build_sass(self, selectors, statement_blocks, SASS = '', original_selector_string = '', level = 0):
        for key, value in selectors.items():
            selector_string = original_selector_string + ' ' + key
            SASS = SASS + "\n\n" + self.__get_n_tabs(level) + key + " {\n"
            css = self.__get_css_for_this_selector(statement_blocks, selector_string)
            if (len(css) > 0):
                'in css replace \n for \n and appropriate amount of tabs'
                css = self.__get_n_tabs(level+1) + css.replace("\n", "\n" + self.__get_n_tabs(level+1))
            SASS = SASS + css
            print value
            '''if (value($children) > 0) {
                $SASS = $this->buildSass($children, $statementBlocks, $SASS, $selectorString, ($level + 1));
                $SASS = $SASS . "\n" . $this->getNtabs($level) . "}";
            } else {
                $SASS = $SASS . "\n" . $this->getNtabs($level) . "}";
            }'''
        return SASS


    '''foreach($selectors as $selector => $children) {
            $selectorString = $originalSelectorString . ' ' . $selector;

            $SASS = $SASS . "\n\n" . $this->getNtabs($level) . $selector . " {\n";

            $css = $this->get_cssForThisSelector($statementBlocks, $selectorString);
            if (strlen($css) > 0) {
                $css = $this->getNtabs($level + 1) . str_replace("\n", "\n" . $this->getNtabs($level + 1), $css);
            }
            $SASS = $SASS . $css;

            if (count($children) > 0) {
                $SASS = $this->buildSass($children, $statementBlocks, $SASS, $selectorString, ($level + 1));
                $SASS = $SASS . "\n" . $this->getNtabs($level) . "}";
            } else {
                $SASS = $SASS . "\n" . $this->getNtabs($level) . "}";
            }
        }
        '''



    def convert_selectors_to_nested_dict(self, selectors):
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



    # Level 2
    def get_statement_blocks (self, all_css_code):
        statement_blocks = []
        regex = re.compile(r"([0-9a-zA-Z#: \.\-_]+\{([^}]*)\})", re.I | re.M);

        for match in regex.finditer(all_css_code):
            statement_blocks.append(match.group(1))

        return statement_blocks

    # Level 2
    def get_selectors (self, all_css_code):
        selectors = []
        regex = re.compile(r"([0-9a-zA-Z#: \.\-_]+){([^}]*)\}", re.I | re.M);

        for match in regex.finditer(all_css_code):
            selectors.append(match.group(1).strip(' \t\n\r'))

        selectors_dict = self.convert_selectors_to_nested_dict(selectors)

        return selectors_dict