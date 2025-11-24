import sys
import subprocess
import threading
import random
from scheduler.reader import dictionary
from time import sleep
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from scheduler.launcher_ui import LauncherUi
from scheduler.db import UnitOfWork
from scheduler.settings import get_settings



class MainWindow(QMainWindow, LauncherUi):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # self.driverButton.clicked.connect(self.run_driver)
        self.parserButton.clicked.connect(self.run_parser)
        # self.parserButton.clicked.connect(self.edit_config)
        self.autoParserButton.clicked.connect(self.run_parser_auto_mode)
        self.numberPageLineEdit.textChanged.connect(self.get_number)
        self.dict = dictionary.Dictionary()

        self.siteComboBox.addItems(self.dict.sites)
        self.typeComboBox.addItems(self.dict.types)
        self.countOfItemOnPageComboBox.addItems(self.dict.nameOfGroupCategories)

        self.siteComboBox.currentIndexChanged.connect(self.get_site)
        self.typeComboBox.currentIndexChanged.connect(self.get_types)
        self.itemComboBox.currentIndexChanged.connect(self.get_item)
        self.countOfItemOnPageComboBox.currentIndexChanged.connect(self.get_page_item_count)

        self.db = UnitOfWork()
        self.is_parser_working = False
        self.is_launcher_working = False
        # self.is_driver_working = False
        self.is_listener_working = False
        self.table_name = None
        self.delay_time_past = None
        self.hours_delay = 0
        self.page = None
        self.parser_process = None
        self.driver_process = None
        self.selectedSite = None
        self.selectedNameOfGroupCategory = None
        self.selectedItem = None
        self.selectedCountOfItemOnPage = None
        self.get_types(0)
        self.get_page_item_count(0)
        self.set_url()
        config = get_settings()
        self.configFile = config["microparser"]["configFile"]
        self.launchDir = config["microparser"]["launchDir"]
        self.config = self.dict.get_config(self.configFile)
        self.run_driver_command()

    def set_url(self):
        label_message = "укажите страницу и деталь"
        if self.page is None:
            label_message = f'"https://www.chipdip.by/catalog-show/{self.selectedItem}?page={self.page}"'
        self.urlLabel.setText(label_message)
        
    # def run_driver(self):
    #
    #     if not self.is_driver_working:
    #         thread = threading.Thread(target=self.run_driver_command)
    #         thread.start()
    #     else:
    #         print(self.driver_process.pid)
    #         self.driver_process.terminate()
    #
    #
    #     self.is_driver_working = not self.is_driver_working
    #     self.driverButton.setText('Отключить' if self.is_driver_working else 'Запустить')
    #     self.driverStatusLabel.setText('Работает' if self.is_driver_working else 'Отключен')

    def run_driver_command(self):
        self.driver_process = subprocess.Popen(
            "ping google.com",
            # 'java "-Dwebdriver.chrome.driver=d:\\work\\selenium136\\chromedriver.exe" -jar "D:\\work\\selenium136\\selenium-server-standalone-3.5.3.jar"',
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        self.driver_process.wait()

    def run_parser(self):
        if self.page is None:
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
        # self.driverButton.setEnabled(not self.is_parser_working)
        self.autoParserButton.setEnabled(not self.is_parser_working)

    
    def edit_config(self):
        print(self.selectedNameOfGroupCategory)
        print(self.page)
        print(self.selectedCountOfItemOnPage)
        self.config['countOfItemOnPage'] = self.selectedCountOfItemOnPage
        self.config['numberOfPage'] = self.page
        self.config['nameOfGroupCategory'] = self.selectedNameOfGroupCategory
        lines = ""
        for key, value in self.config.items():
            print(key)
            print(value)
            lines += f"{key} = {value}\n"

        with open(self.configFile, "w") as config:
            config.write(lines)

    def stop_parser(self):
        subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=self.parser_process.pid))

    def run_parser_command(self):
        self.numberPageLineEdit.setEnabled(False)
        self.siteComboBox.setEnabled(False)
        self.typeComboBox.setEnabled(False)
        self.itemComboBox.setEnabled(False)
        self.countOfItemOnPageComboBox.setEnabled(False)
        self.parser_process = subprocess.Popen(
            "ping google.com",
            # "mvn test -Dsuite=testng",
            cwd=self.launchDir,
            shell=True
        )

        self.parser_process.wait()
        print(self.parser_process.returncode)

        self.is_parser_working = False
        print(f"парсер статус {self.parser_process.returncode}")

        self.parserStatusLabel.setText("Отключен")
        self.parserButton.setText("Запустить")
        if not self.is_launcher_working:
            self.autoParserButton.setEnabled(True)
            self.parserButton.setEnabled(True)
            self.countOfItemOnPageComboBox.setEnabled(True)
            # self.driverButton.setEnabled(True)
            self.numberPageLineEdit.setEnabled(True)
            self.siteComboBox.setEnabled(True)
            self.typeComboBox.setEnabled(True)
            self.itemComboBox.setEnabled(True)
        self.db.insert_many(table_name=self.table_name)

    def run_parser_auto_mode(self):
        if self.page is None:
            msgBox = QMessageBox()
            msgBox.setText("Выберите страницу и тип элемента")
            msgBox.exec()
            return

        if not self.is_launcher_working:
            thread = threading.Thread(target=self.run_auto_mode)
            thread.start()
        else:
            self.stop_parser()
            self.is_listener_working = False

        self.is_launcher_working = not self.is_launcher_working
        self.parserButton.setEnabled(not self.is_launcher_working)
        # self.driverButton.setEnabled(not self.is_launcher_working)
        self.autoParserStatusLabel.setText('Работает' if self.is_launcher_working else 'Отключен')
        self.autoParserButton.setText('Отключить' if self.is_launcher_working else 'Запустить')
        self.numberPageLineEdit.setEnabled(not self.is_launcher_working)
        self.siteComboBox.setEnabled(not self.is_launcher_working)
        self.typeComboBox.setEnabled(not self.is_launcher_working)
        self.itemComboBox.setEnabled(not self.is_launcher_working)
        self.countOfItemOnPageComboBox.setEnabled(not self.is_launcher_working)

    def run_auto_mode(self):
        if self.page is None:
            msgBox = QMessageBox()
            msgBox.setText("Выберите страницу и тип элемента")
            msgBox.exec()
            return

        self.delay_time_past = True
        self.hours_delay = 0
        self.is_listener_working = True
        self.autoParserButton.setText('Отключить')
        label_message = ""
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

            if self.parser_process.returncode == 1:
                self.hours_delay = random.randint(6, 10)
                label_message = f"Выполнено, выжидает интервал перед следущим запуском {self.hours_delay} часов"
                self.page = f'{int(self.page)+1}'
                self.numberPageLineEdit.setText(self.page)
                self.edit_config()
                self.delay_time_past = True
                self.db.insert_many(table_name=self.table_name)
            elif self.parser_process.returncode is not None:
                label_message = "Отключен"

            print(f"слушатель {self.parser_process.returncode}")
            self.autoParserStatusLabel.setText(label_message)

    def get_number(self):
        if not hasattr(self, 'page'):
            self.page = ''

        if self.numberPageLineEdit.text().isdigit():
            self.page = self.numberPageLineEdit.text()

        elif self.numberPageLineEdit.text() != self.page:
            if self.numberPageLineEdit.text() == '':
                self.page = ''
            self.numberPageLineEdit.setText(self.page)
        self.set_url()

    def get_site(self, index):
        self.selectedSite = self.siteComboBox.itemText(index)

    def get_item(self, index):
        self.selectedItem = self.itemComboBox.itemText(index)
        # self.selectedItem = index
        self.set_url()

    def get_types(self, index):
        self.table_name = self.dict.types[index]
        self.itemComboBox.clear()
        print(self.dict.types[index])
        self.itemComboBox.addItems(self.dict.items[index].get(self.table_name))
        self.selectedNameOfGroupCategory = index + 1
        self.get_item(0)

    def get_page_item_count(self, index):
        self.selectedCountOfItemOnPage = self.countOfItemOnPageComboBox.itemText(index)
        

def start():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
