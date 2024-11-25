import db_oim_orm
class Dictionary:
    items = []
    types = []
    sites = []
    def __init__(self):
        #load info rom site
        self.items = [
            {db_oim_orm.Microchips.__tablename__ : [
                "ic-ac-dc-converters",
                "ic-dc-dc-converters",
                "rmc-dc-converters",
                "v-f-and-f-v-converters",
                "ic-analog-switch"
            ]},
            {db_oim_orm.Resistors.__tablename__: [
                "rezistory",
                "resistors-2w",
                "smd-resistors",
                "potentiometers",
                "trimmer-potentiometers"
            ]},
            {db_oim_orm.Diods.__tablename__: [
                "diodes-zener",
                "diodes-schottky",
                "diodes-power-rus",
                "diodes-uhf-rus",
                "diodes-other",
            ]},
            {db_oim_orm.Capacitors.__tablename__: [
                "hv-ceramic-capacitors",
                "disc-ceramic-capacitors",
                "smd-capacitors",
                "monolithic-ceramic-capacitors",
                "metallized-paper-capacitors"
            ]},
            {db_oim_orm.Transistors.__tablename__: [
                "bipolar-transistors",
                "field-effect-transistor",
                "igbt",
                "jfet-transistors",
                "digital-transistors"
            ]}
        ]
        self.types = [
            db_oim_orm.Microchips.__tablename__,
            db_oim_orm.Resistors.__tablename__,
            db_oim_orm.Diods.__tablename__,
            db_oim_orm.Capacitors.__tablename__,
            db_oim_orm.Transistors.__tablename__
        ]
        self.sites = [
            "www.chipdip.by",
            "www.belchip.by"
        ]