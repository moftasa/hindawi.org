# hindawi.org
Scripts that manipulate Hindawi.org ebooks

## fix-hindawi-epub.py

I emailed hindawi.org about the unnecessary fonts in their ebooks making the files much larger than neccessary. There is an embded Chinese SimSun.ttf font that is 10MB in size uncompressed. They replied that they would do something about it but they never did.

What this poorly written script does is open a Hindawi.org epub file and removes unnecessary fonts. The necessary fonts are the one referenced in the CSS. This script reduces the size of an ebook (from an average of 9MB to ~1MB).

__Note:__ This only works on Hindawi files for now as there are no agreed upon location for CSS files or fonts in the EPUB standard.

Usage: fix-hindawi-epub.py filename.epub

Output: fixed_filename.epub
