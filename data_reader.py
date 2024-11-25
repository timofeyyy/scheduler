import db_oim_orm
class Reader:
    data = []
    classes = {}
    def __init__(self):
        # will be from json
        self.classes = {
            "Microchip": {
                "object": db_oim_orm.Microchips,
                "properties": {
                    "id": "ID",
                    "docId": "DocID",
                    "componentName": "ComponentName",
                    "componentType": "Type_ID",
                    "componentKind": "Kind_ID",
                    "manufacturer":  "ManufacturerName_ID",
                    "interfaceName": "Interfaces",
                    "voltageMin": "MinVoltage",
                    "voltageMax": "MaxVoltage",
                    "frequency": "Frequency",
                    "bitDepth": "BitDepthValue",
                    "consumptionCurrent": "ConsumptionCurrent",
                    "technology": "TechnologyName_ID",
                    "temperatureMin": "MinOperatingTemperature",
                    "temperatureMax": "MaxOperatingTemperature",
                    "radiationResistance": "RadiationResistance",
                    "radiationResistanceMeasures": "RadiationResistanceI",
                    "memoryFormat": "MemoryFormat",
                    "samplingTime": "SamplingTime",
                    "packageType": "Package",
                    "qualification": "Qualication",
                    "remark1": "Remark1"
                } 
            },
        }
        # print(self.classes["Microchip"]["properties"]["id"])
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
                obj = self.classes[name]["object"]()
                properties = data.split(",")

                for property in properties:
                    key_value = property.split("=")
                    key = key_value[0].replace(" ", "")
                    if key in self.classes[name]["properties"]:
                        value = key_value[1]

                        if value == "null" or value == "'null'":
                            value = None
                        setattr(obj, self.classes[name]["properties"][key], value)

                        # print(key + "\t" + value)
                        # print("\n")
                    self.data.append(obj)

    def print(self):
        for _ in self.data:
            print(getattr(_, "ComponentName"))
            print("\n")





