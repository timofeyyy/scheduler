import sys
import subprocess
import threading
import random
from time import sleep

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from launcher_ui import Ui



class MainWindow(QMainWindow, Ui):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.driverBtn.clicked.connect(self.run_driver)
        self.parserBtn.clicked.connect(self.run_parser)
        self.launchBtn.clicked.connect(self.run_launcher)
        self.numberLineEdit.textChanged.connect(self.get_number)
        self.comboBox.currentIndexChanged.connect(self.get_type)
        self.button_status = [ "Отключить", "Запустить"]



    def run_driver(self):
        # for example invalid status 1 depend on command status
        if not hasattr(self, 'driver_status'):
            self.driver_status = 1

        if self.driver_status == 1 :
            self.driver_status_label.setText("Работает")
            self.driver_status = 0
            thread = threading.Thread(target=self.run_driver_command)
            thread.start()
        else:
            self.driver_process.terminate()
            self.driver_status_label.setText("Отключен")
            self.driver_status = 1

        self.driverBtn.setText(self.button_status[self.driver_status])

    def print_stdout(self, lines):
        for line in lines:
            print(line.strip())

    def run_driver_command(self):
        self.driver_process = subprocess.Popen(
            "ping google.com -n 10",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='cp866'
        )
        self.print_stdout(self.driver_process.stdout)




        label_message = "Отключен"

        self.driver_process.wait()
        if self.driver_process.returncode == 1:
            label_message = "Комманда завершилась с ошибкой или была прервана"

        self.driver_status = 1
        print(self.driver_process.returncode)

        self.driver_status_label.setText(label_message)
        self.driverBtn.setText(self.button_status[self.driver_status])






    def run_parser(self):
        if not hasattr(self, 'page') or not hasattr(self, 'selectedItem'):
            msgBox = QMessageBox()
            msgBox.setText("Выберите страницу и тип элемента")
            ret = msgBox.exec()
            return

        # for example invalid status 1 depend on command status
        if not hasattr(self, 'parser_status'):
            self.parser_status = 1

        if self.parser_status == 1:
            self.edit_config()
            self.parser_status_label.setText("Работает")
            self.parser_status = 0
            thread = threading.Thread(target=self.run_parser_command)
            thread.start()
        else:
            self.parser_process.terminate()
            self.parser_status_label.setText("Отключен")
            self.parser_status = 1

        self.parserBtn.setText(self.button_status[self.parser_status])

    def edit_config(self):
        print(self.page)
        with open("config.properties", "r") as config:
            content = config.read()
            params = content.split("\n")
            # print(params)
            for i in range(len(params)):
                key_value = params[i].split("=")
                key = key_value[0].replace(" ", "")
                if key == "url":
                    key_value[1] = f'"https://metanit.com/python/tutorial/{self.page}.php"'
                params[i] = '= '.join(key_value)

            content = '\n'.join(params)

        with open("config.properties", "w") as config:
            config.write(content)



    def run_parser_command(self):
        self.parser_process = subprocess.Popen(
            "ping google.com -n 10",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='cp866'
        )
        self.print_stdout(self.parser_process.stdout)
        label_message = "Отключен"

        self.parser_process.wait()
        if self.parser_process.returncode == 1:
            label_message = "Комманда завершилась с ошибкой или была прервана"

        self.parser_status = 1
        print(self.parser_process.returncode)

        self.parser_status_label.setText(label_message)
        self.parserBtn.setText(self.button_status[self.parser_status])

    def run_launcher(self):
        if not hasattr(self, 'launcher_status'):
            self.launcher_status = 1

        label_message = "Отключен"

        if not hasattr(self, 'is_working') or not self.is_working:
            self.launcher_status = 0
            label_message = "Работает"
            thread = threading.Thread(target=self.run_launcher_command)
            thread.start()
        else:
            self.launcher_status = 1
            self.launcher_process.terminate()
            self.is_working = False

        self.launch_status_label.setText(label_message)
        self.launchBtn.setText(self.button_status[self.launcher_status])


    def run_launcher_command(self):
        self.launcher_status = 0
        self.hours_delay = 0
        self.is_working = True

        while self.is_working:
            if not self.launcher_status == None:
                if self.hours_delay != 0:
                    sleep(self.hours_delay) # * 60 * 60

                thread = threading.Thread(target=self.wait_launcher_end)
                thread.start()
                self.hours_delay = random.randint(6, 10)
                self.launcher_status = None

            sleep(2)


    def wait_launcher_end(self):
        self.launcher_process = subprocess.Popen("ping google.com -n 10", creationflags=subprocess.CREATE_NEW_CONSOLE)
        self.launcher_process.wait()
        self.launcher_status = self.launcher_process.returncode

        label_message = f"Выполнено, выжидае интервал перед следущим запуском {self.hours_delay} часов"
        # if we break ping operation in the middle of processing we will get status 0 which is mean good status and that is why we will have Отключено instead of Комманда завершилась с ошибкой или была прервана
        if self.launcher_status == 1:
            label_message = "Комманда завершилась с ошибкой или была прервана"
            self.is_working = False

        print(self.launcher_status)
        self.launch_status_label.setText(label_message)
        self.launchBtn.setText(self.button_status[self.launcher_status])


    def get_number(self):
        if not hasattr(self, 'page'):
            self.page = ''

        if self.numberLineEdit.text().isdigit():
            self.page = self.numberLineEdit.text()

        elif self.numberLineEdit.text() != self.page:
            if self.numberLineEdit.text() == '':
                self.page = ''
            self.numberLineEdit.setText(self.page)

    def get_type(self, index):
        self.selectedItem = self.comboBox.itemText(index)

def start():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
