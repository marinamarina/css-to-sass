#!/usr/bin/python

from converter.convert import CssToSassConverter

statement_string='''#my_element h1 {
    font-weight: bold;
}

#my_element ul.test {
    list-style-type: none
}

#my_element ul.test {
    color: white;
    background: black;
}

#my_element ul.test .list-item {
    text-decoration: none;
    color: #737373;
}

#my_element ul.test .list-item:last-child {
    font-weight: bold;
}'''

converter = CssToSassConverter()

print converter.convert(statement_string)

