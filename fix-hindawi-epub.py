#!/usr/bin/env python3

# Opens a Hindawi.org epub file and removes unnecessary fonts
# The necessary fonts are the one referenced in the CSS file
# This only works on Hindawi files for now as there are no standard location for CSS files or fonts in the EPUB standard
# This script manages to reduce the size of a book considerably (from ~9MB to ~1MB)
#
# Usage: fix-hindawi-epub.py filename.epub
# Output: fixed_filename.epub

import sys
import zipfile
import re
import os

# get the directory and filename
filepath = sys.argv[1]
directory = os.path.dirname(filepath)
filename = os.path.basename(filepath)

# Open epub/zip file and read CSS
epub = zipfile.ZipFile(filepath, 'r')
epub_css = epub.read('EPUB/Style/epub.css').decode("utf-8")

#create output epub/zip file
new_filename = os.path.join(directory, 'fixed_' + filename)
epub_out = zipfile.ZipFile(new_filename, 'w')

# Split CSS to avoid overlapping matches when running regex
css = epub_css.split(";")

fonts = []
fontString = '(../Fonts/.*.ttf)'

for part in css:
    fonts += re.findall(fontString, part)

list_of_fonts = []

for font in fonts:
    font = re.sub('\.\./', 'EPUB/', font)
    list_of_fonts.append(font)

for item in epub.infolist():
    buffer = epub.read(item.filename)
    if item.filename[:10] == "EPUB/Fonts":
        if item.filename in list_of_fonts:
            epub_out.writestr(item, buffer)
    else:
        epub_out.writestr(item, buffer)

epub_out.close()
epub.close()


