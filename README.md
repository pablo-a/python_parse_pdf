# python_parse_pdf
---------------------------
### let's try to parse a pdf document using python PDFMiner module

- First try with **PDFMiner** :
    - all data is here but bad formatted (because it is in a table i guess)
- **Poppler** for Linux : `pdf2html -xml input.pdf output.xml` (`sudo apt-get install poppler-utils`)
    - the result looks good, need some regex to extract the data.
    - the function `pdf2text` works well but no what i want (cool for keeping layout though)
