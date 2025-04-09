
import launcher
from reader.pdf_parser import PDFParser

# launcher.start()
# reader = Reader()
# records = reader.fetch()
# reader.print()

pdfParser = PDFParser(
    "D:\\work\\scheduler\\scheduler\\src\\datasheets.txt"
)

pdfParser.read()
pdfParser.download()


