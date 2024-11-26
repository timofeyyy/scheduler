import json
from db_oim_orm import (Microchips)
class Reader:
    data = []
    classes = {}
    module = None
    def __init__(self):
        with open('item_properties.json', 'r') as file:
            self.classes = json.load(file)

        self.module = __import__('db_oim_orm')



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
        with open("D:\\work\\home\\componentsFile6.txt", "r") as components:
            content = components.read()
            lines = content.split("\n")
            lines.pop()

            for line in lines:
                name_data = line.split("{")
                name = name_data[0]
                data = name_data[1].replace("}", "")

                obj = getattr(self.module, self.classes[name]["object"])()

                properties = data.split(",")
                last_saved_key = None
                for property in properties:
                    key_value = property.split("=")

                    key = key_value[0].replace(" ", "")

                    if key in self.classes[name]["properties"]:
                        # print("if\t"+key)
                        value = key_value[1]
                        last_saved_key = key
                        if value == "null" or value == "'null'":
                            value = None
                        setattr(obj, self.classes[name]["properties"][key], value)
                    elif last_saved_key is not None:
                        setattr(
                            obj,
                            self.classes[name]["properties"][last_saved_key],
                            getattr(obj, self.classes[name]["properties"][last_saved_key])
                            + ", "
                            + key
                        )
                self.data.append(obj)


    def print(self):
        print(len(self.data))
        for _ in self.data:
            print(getattr(_, "ID"))
            print(getattr(_, "DocID"))
            print(getattr(_, "ComponentName"))
            print(getattr(_, "Type_ID"))
            print(getattr(_, "Kind_ID"))
            print(getattr(_, "ManufacturerName_ID"))
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





