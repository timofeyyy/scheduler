import json
from scheduler.settings import get_settings
from scheduler.db import db_oim_orm


class Reader:
    data = []
    propertyConfig = {}

    def __init__(self):
        config = get_settings()
        self.txtDir = config['data']['txtDir']
        with open(config['project']['configFile'], 'r') as file:
            self.propertyConfig = json.load(file)
        self.module = db_oim_orm

    def fetch(self, table_name):
        if table_name in self.propertyConfig and "fileName" in self.propertyConfig[table_name]:
            self.data.clear()
            filepath = f"{self.txtDir}\\{self.propertyConfig[table_name]['fileName']}"
            with open(filepath, "r", encoding='UTF-8') as components:
                content = components.read()
                # print(content)
                lines = content.split("\n")
                # print(lines[0])

                lines.pop()
                # print(len(lines))

                for line in lines:
                    name_data = line.split("{")
                    # name = name_data[0]
                    data = name_data[1].replace("}", "")
                    # print(name)
                    # print(name in self.propertyConfig)
                    # print(self.propertyConfig[tableName])
                    obj = getattr(self.module, table_name)()

                    properties = data.split(",")
                    last_saved_key = None
                    for property in properties:
                        key_value = property.split("=")

                        key = key_value[0].replace(" ", "")

                        if key in self.propertyConfig[table_name]["properties"]:
                            value = key_value[1]
                            value = value.replace("'","")
                            last_saved_key = key
                            if value == "null":
                                value = None
                            setattr(obj, self.propertyConfig[table_name]["properties"][key], value)
                        elif last_saved_key is not None:
                            setattr(
                                obj,
                                self.propertyConfig[table_name]["properties"][last_saved_key],
                                getattr(obj, self.propertyConfig[table_name]["properties"][last_saved_key])
                                + ", "
                                + key
                            )
                    self.data.append(obj)
            return self.data
        return None

    # def clear(self):
    #     with open(self.filepath, 'w'):
    #         pass

    # def getFncName(self, tableName):
    #     if tableName in self.propertyConfig and "fetchDelegateName" in self.propertyConfig[tableName]:
    #         return self.propertyConfig[tableName]["fetchDelegateName"]
    #     return None

    def print(self):
        print(len(self.data))
        for _ in self.data:
            print(vars(_))
            print("\n")






