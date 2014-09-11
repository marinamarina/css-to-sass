#!/usr/bin/python

from my_app.convert import CssToSassConverter

statement_string='''.foo .bar p {
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

converter = CssToSassConverter()

print converter.get_statement_blocks(statement_string)

