from scheduler.db.repo import db_oim_orm
from scheduler.reader.alias_ref import data_ref
from scheduler.settings import get_settings


class Reader:

    def __init__(self):
        settings = get_settings()
        self.txtDir = settings['data']['txtDir']
        self.module = db_oim_orm

    def fetch(self, table_name):
        if table_name in data_ref and "fileName" in data_ref[table_name]:
            records = []
            filepath = f"{self.txtDir}\\{data_ref[table_name]['fileName']}"
            with open(filepath, "r", encoding='UTF-8') as components:
                content = components.read()
                lines = content.split("\n")
                lines.pop()
                for line in lines:
                    name_data = line.split("{")
                    data = name_data[1].replace("}", "")
                    obj = getattr(self.module, table_name)()
                    properties = data.split(",")
                    for property in properties:
                        key_value = property.split("=")
                        key = key_value[0].replace(" ", "")
                        if key in data_ref[table_name]["properties"]:
                            value = key_value[1]
                            value = value.replace("'","")
                            if value == "null":
                                value = None
                            setattr(obj, data_ref[table_name]["properties"][key], value)
                    records.append(obj)
            return records
        return None







