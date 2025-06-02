import requests
from pathlib import Path

class PDFParser:
    def __init__(self, datasheetPath):
        self.datasheetPath = datasheetPath
        self.list = []

    def read(self):
        with open(self.datasheetPath, 'r') as content:
            links = content.read()
            self.list = links.split(",")

    def download(self, link):
        name = None
        try:
            dotParts = link.split('.')
            slashParts = dotParts[len(dotParts) - 2].split('/')
            name = slashParts[len(slashParts) - 1]
            filePath = f'{self.datasheetPath}\\{name}.pdf'
            file = Path(filePath)
            if not file.exists():
                bytes = requests.get(link)
                with open(filePath, 'wb') as f:
                    f.write(bytes.content)
                print(f"downloaded {name}")
        except:
            pass
        return name
