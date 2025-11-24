import os
import shutil
import requests
from pathlib import Path

from scheduler.settings import get_settings


# from scheduler.db import ComponentFamilyBase


class PDFStorage:
    def __init__(self):
        settings = get_settings()
        self.datasheet_path = settings['pdf']['storeDir']

    def download(self, catalog, link):
        print(catalog)
        name = None
        try:
            dot_parts = link.split('.')
            slash_parts = dot_parts[len(dot_parts) - 2].split('/')
            name = slash_parts[len(slash_parts) - 1]
            file_path = f'{self.datasheet_path}\\{catalog}\\{name}.pdf'
            file = Path(file_path)
            if not file.exists():
                bytes = requests.get(link)
                with open(file_path, 'wb') as f:
                    f.write(bytes.content)
                print(f"downloaded {name}")
            else:
                print(f"file ${name} already exists")
        except:
            pass
        return name

    def store_as_catalog_refactor(self, repository):
        rows: list = repository.select_all_wrap()
        dir_path = f"{self.datasheet_path}//{repository.__typename__}"
        print(len(rows))
        if os.path.isdir(dir_path):
            print(f"The directory '{dir_path}' exists.")
        else:
            os.mkdir(dir_path)

        files = os.listdir(self.datasheet_path)
        for file in files:
            for row in rows:
                if row.SpecificationDoc is not None and row.SpecificationDoc in file:
                    existed_path = f"{self.datasheet_path}//{file}"
                    new_path = f"{dir_path}//{file}"
                    shutil.copyfile(existed_path, new_path)
                    break
