#!/usr/bin/python

import sys
from converter.convert import CssToSassConverter

if len(sys.argv) == 3:
    inname, outname = sys.argv[1:3]
    converter = CssToSassConverter(css_file=inname, sass_file=outname)
else:
  converter = CssToSassConverter()

if __name__ == "__main__":
    converter.write_results_to_file()
