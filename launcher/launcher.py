import sys
import subprocess
import threading
import random

from db.db_session import DBSession
from launcher.launcher_ui import LauncherUI
from reader import dictionary

from time import sleep
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox




class MainWindow(QMainWindow, LauncherUI):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup(self)
        self.parserButton.clicked.connect(self.run_parser)
        self.autoParserButton.clicked.connect(self.run_launcher)
        self.numberPageLineEdit.textChanged.connect(self.get_page)
        self.hoursFromLineEdit.textChanged.connect(self.get_hours_from)
        self.hoursToLineEdit.textChanged.connect(self.get_hours_to)

        self.dict = dictionary.Dictionary()

        self.siteComboBox.addItems(self.dict.sites)
        self.typeComboBox.addItems(self.dict.types)

        self.siteComboBox.currentIndexChanged.connect(self.get_site)
        self.typeComboBox.currentIndexChanged.connect(self.set_items)
        self.itemComboBox.currentIndexChanged.connect(self.get_item)

        self.set_items(0)
        self.set_url()

        self.db = DBSession()

        self.is_parser_working = False
        self.is_launcher_working = False

        self.configPath = "D:\\work\\scheduler\\scheduler\\src\\config.properties"

    def set_url(self):
        label_message = "укажите страницу и деталь"
        if self.page_required():
            label_message = f'"https://www.chipdip.by/catalog-show/{self.selectedItem}?page={self.page}"'
        self.urlLabel.setText(label_message)

    def run_parser(self):
        if not self.page_required():
            msgBox = QMessageBox()
            msgBox.setText("Выберите страницу и тип элемента")
            msgBox.exec()
            return

        if not self.is_parser_working:
            self.edit_config()
            thread = threading.Thread(target=self.run_parser_command)
            thread.start()
        else:
            self.stop_parser()

        self.is_parser_working = not self.is_parser_working

        self.parserButton.setText('Отключить' if self.is_parser_working else 'Запустить')
        self.parserStatusLabel.setText('Работает' if self.is_parser_working else 'Отключен')
        self.autoParserButton.setEnabled(not self.is_parser_working)



    def page_required(self):
        return hasattr(self, 'page') and self.page != ''
    def hours_from_required(self):
        return hasattr(self, 'hours_from') and self.hours_from != ''
    def hours_to_required(self):
        return hasattr(self, 'hours_to') and self.hours_to != ''
    def is_interval_invalid(self):
        return int(self.hours_to) <= int(self.hours_from)



    def edit_config(self):
        print(self.page)
        with open(self.configPath, "r") as config:
            content = config.read()
            params = content.split("\n")
            for i in range(len(params)):
                key_value = params[i].split(" = ")
                key = key_value[0].replace(" ", "")
                if key == "baseUrlPageNum":
                    key_value[1] = f'"https://www.chipdip.by/catalog-show/{self.selectedItem}?page={self.page}"'
                params[i] = " = ".join(key_value)
            content = "\n".join(params)

        with open(self.configPath, "w") as config:
            config.write(content)
    def stop_parser(self):
        subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=self.parser_process.pid))
    def run_parser_command(self):
        self.numberPageLineEdit.setEnabled(False)
        self.siteComboBox.setEnabled(False)
        self.typeComboBox.setEnabled(False)
        self.itemComboBox.setEnabled(False)
        self.parser_process = subprocess.Popen(
            "ping google.com",
            shell=True
        )
        self.parser_process.wait()
        print(self.parser_process.returncode)
        label_message = "Отключен"

        self.is_parser_working = False
        print(f"парсер статус {self.parser_process.returncode}")

        self.parserStatusLabel.setText(label_message)
        self.parserButton.setText("Запустить")
        if not self.is_launcher_working:
            self.autoParserButton.setEnabled(True)
            self.parserButton.setEnabled(True)
            self.numberPageLineEdit.setEnabled(True)
            self.siteComboBox.setEnabled(True)
            self.typeComboBox.setEnabled(True)
            self.itemComboBox.setEnabled(True)
    def run_launcher(self):
        msgBox = QMessageBox()

        if not self.page_required():
            msgBox.setText("Выберите страницу и тип элемента")
            msgBox.exec()
            return

        if not self.hours_from_required() or not self.hours_to_required():
            msgBox.setText("Укажите интервал (оба поля должны быть заполнены)")
            msgBox.exec()
            return

        if self.is_interval_invalid():
            msgBox.setText("Некоректный интервал")
            msgBox.exec()
            return

        if not self.is_launcher_working:
            thread = threading.Thread(target=self.run_listener)
            thread.start()
        else:
            self.stop_parser()
            self.is_listener_working = False


        self.is_launcher_working = not self.is_launcher_working
        self.parserButton.setEnabled(not self.is_launcher_working)
        self.autoParserStatusLabel.setText('Работает' if self.is_launcher_working else 'Отключен')
        self.autoParserButton.setText('Отключить' if self.is_launcher_working else 'Запустить')
        self.numberPageLineEdit.setEnabled(not self.is_launcher_working)
        self.siteComboBox.setEnabled(not self.is_launcher_working)
        self.typeComboBox.setEnabled(not self.is_launcher_working)
        self.itemComboBox.setEnabled(not self.is_launcher_working)
        self.hoursToLineEdit.setEnabled(not self.is_launcher_working)
        self.hoursFromLineEdit.setEnabled(not self.is_launcher_working)
    def run_listener(self):


        self.delay_time_past = True
        self.hours_delay = 0
        self.is_listener_working = True
        self.autoParserButton.setText('Отключить')

        while self.is_listener_working:
            if self.delay_time_past:
                if self.hours_delay != 0:
                        sleep(self.hours_delay)
                        if not self.is_listener_working:
                            break

                thread = threading.Thread(target=self.run_parser_command)
                thread.start()
                label_message = 'Работает'
                self.delay_time_past = False

            sleep(1)


            if self.parser_process.returncode == 0:
                self.hours_delay = random.randint(int(self.hours_from), int(self.hours_to))
                label_message = f"Выполнено, выжидает интервал перед следущим запуском {self.hours_delay} часов"
                self.page = f'{int(self.page)+1}'
                self.numberPageLineEdit.setText(self.page)
                self.edit_config()
                self.delay_time_past = True
                self.db.insertRowsFromFile()


            elif self.parser_process.returncode != None:
                label_message = "Отключен"

            print(f"слушатель {self.parser_process.returncode}")
            self.autoParserStatusLabel.setText(label_message)

    def get_page(self):
        if not hasattr(self, 'page'):
            self.page = ''

        if self.numberPageLineEdit.text().isdigit():
            self.page = self.numberPageLineEdit.text()

        elif self.numberPageLineEdit.text() != self.page:
            if self.numberPageLineEdit.text() == '':
                self.page = ''
            self.numberPageLineEdit.setText(self.page)
        self.set_url()

    def get_hours_from(self):
        if not hasattr(self, 'hours_from'):
            self.hours_from = ''

        if self.hoursFromLineEdit.text().isdigit():
            self.hours_from = self.hoursFromLineEdit.text()

        elif self.hoursFromLineEdit.text() != self.hours_from:
            if self.hoursFromLineEdit.text() == '':
                self.hours_from = ''
            self.hoursFromLineEdit.setText(self.hours_from)

    def get_hours_to(self):
        if not hasattr(self, 'hours_to'):
            self.hours_to = ''

        if self.hoursToLineEdit.text().isdigit():
            self.hours_to = self.hoursToLineEdit.text()

        elif self.hoursToLineEdit.text() != self.hours_to:
            if self.hoursToLineEdit.text() == '':
                self.hours_to = ''
            self.hoursToLineEdit.setText(self.hours_to)


    def get_site(self, index):
        self.selectedSite = self.siteComboBox.itemText(index)

    def get_item(self, index):
        self.selectedItem = self.itemComboBox.itemText(index)
        self.set_url()

    def set_items(self, index):
        self.itemComboBox.clear()
        self.itemComboBox.addItems(self.dict.items[index].get(self.dict.types[index]))
        self.get_item(0)

def start():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
