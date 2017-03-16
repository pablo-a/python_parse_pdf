# python_parse_pdf
---------------------------
### let's try to parse a pdf document using python PDFMiner module

- First try with **PDFMiner** :
    - all data is here and really good formatted
- **Poppler** for Linux : `pdf2html -xml input.pdf output.xml` (`sudo apt-get install poppler-utils`)
    - the result looks good, need some regex to extract the data.
    - the function `pdftotext -layout input.pdf output.txt` works well, may be what i want (pdfminer.txt)
