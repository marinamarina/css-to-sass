#!/usr/bin/python

import sys
from converter.convert import CssToSassConverter

if len(sys.argv) == 3:

    # create files dictionary comprehension
    # using filename from CssToSassConverter.default_options as a key
    # and command line arguments as a value
    files = {filename_key : sys.argv[index+1]
             for index, filename_key
             in enumerate(CssToSassConverter.default_options)
    }

    # unpacking the dictionary files, providing user chosen filenames
    converter = CssToSassConverter(**files)
else:
  converter = CssToSassConverter()

if __name__ == "__main__":
    converter.write_results_to_file()
