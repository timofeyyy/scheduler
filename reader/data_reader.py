import json

from db import db_oim_orm


class Reader:
    data = []
    propertyConfig = {}
    def __init__(self, propPath, dataPath):
        with open(propPath, 'r') as file:
            self.propertyConfig = json.load(file)
        # print(self.propertyConfig)
        self.module = db_oim_orm
        self.filepath = dataPath




        # self.classes = {
        #     "Microchip": {
        #         "object": Microchips,
        #         "properties": {
        #             "id": "ID",
        #             "docId": "DocID",
        #             "componentName": "ComponentName",
        #             "componentType": "Type_ID",
        #             "componentKind": "Kind_ID",
        #             "manufacturer":  "ManufacturerName_ID",
        #             "interfaceName": "Interfaces",
        #             "voltageMin": "MinVoltage",
        #             "voltageMax": "MaxVoltage",
        #             "frequency": "Frequency",
        #             "bitDepth": "BitDepthValue",
        #             "consumptionCurrent": "ConsumptionCurrent",
        #             "technology": "TechnologyName_ID",
        #             "temperatureMin": "MinOperatingTemperature",
        #             "temperatureMax": "MaxOperatingTemperature",
        #             "radiationResistance": "RadiationResistance",
        #             "radiationResistanceMeasures": "RadiationResistanceI",
        #             "memoryFormat": "MemoryFormat",
        #             "samplingTime": "SamplingTime",
        #             "packageType": "Package",
        #             "qualification": "Qualication",
        #             "remark1": "Remark1"
        #         }
        #     },
        # }
    def fetch(self):

        self.data.clear()
        with open(self.filepath, "r", encoding='UTF-8') as components:
            content = components.read()
            print(content)
            lines = content.split("\n")
            print(lines[0])

            lines.pop()
            print(len(lines))

            for line in lines:
                name_data = line.split("{")
                name = name_data[0]
                data = name_data[1].replace("}", "")
                obj = getattr(self.module, self.propertyConfig[name]["object"])()

                properties = data.split(",")
                last_saved_key = None
                for property in properties:
                    key_value = property.split("=")

                    key = key_value[0].replace(" ", "")

                    if key in self.propertyConfig[name]["properties"]:
                        # print("if\t"+key)
                        value = key_value[1]
                        value = value.replace("'","")
                        last_saved_key = key
                        if value == "null":
                            value = None
                        setattr(obj, self.propertyConfig[name]["properties"][key], value)
                    elif last_saved_key is not None:
                        setattr(
                            obj,
                            self.propertyConfig[name]["properties"][last_saved_key],
                            getattr(obj, self.propertyConfig[name]["properties"][last_saved_key])
                            + ", "
                            + key
                        )
                self.data.append(obj)
        return self.data

    def clear(self):
        with open(self.filepath, 'w'):
            pass

    def print(self):
        print(len(self.data))
        for _ in self.data:
            print(getattr(_, "ID"))
            print(getattr(_, "DocID"))
            print(getattr(_, "ComponentName"))
            print(getattr(_, "Type"))
            print(getattr(_, "Kind"))
            print(getattr(_, "ManufacturerName"))
            print(getattr(_, "Interfaces"))
            print(getattr(_, "MinVoltage"))
            print(getattr(_, "MaxVoltage"))
            print(getattr(_, "Frequency"))
            print(getattr(_, "BitDepthValue"))
            print(getattr(_, "ConsumptionCurrent"))
            print(getattr(_, "TechnologyName_ID"))
            print(getattr(_, "MinOperatingTemperature"))
            print(getattr(_, "MaxOperatingTemperature"))
            print(getattr(_, "RadiationResistance"))
            print(getattr(_, "RadiationResistanceI"))
            print(getattr(_, "MemoryFormat"))
            print(getattr(_, "SamplingTime"))
            print(getattr(_, "Package"))
            print(getattr(_, "Qualication"))
            print(getattr(_, "Remark1"))
            print("\n")





