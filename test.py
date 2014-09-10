#!/usr/bin/python

from convert import CssToSassConverter
import string
import re

converter = CssToSassConverter()
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

print converter.convert(statement_string)

