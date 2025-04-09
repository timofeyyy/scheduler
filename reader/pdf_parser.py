import requests

class PDFParser:
    def __init__(self, datasheetPath):
        self.datasheetPath = datasheetPath
        self.list = []

    def read(self):
        with open(self.datasheetPath, 'r') as content:
            links = content.read()
            self.list = links.split(",")

    def download(self):
        print(len(self.list))
        for line in self.list:
            try:
                # temporary names
                bytes = requests.get(line)
                # print(bytes.text)
                dotParts = line.split('.')
                slashParts = dotParts[len(dotParts)-2].split('/')
                name = slashParts[len(slashParts)-1]
                with open(f'D:\\work\\scheduler\\scheduler\\src\\datasheets\\{name}.pdf', 'wb') as f:
                    f.write(bytes.content)
            except:
                pass
