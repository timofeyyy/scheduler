import sys
import os
import signal
import subprocess
import threading
import psutil
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
        self.get_type(0)

    def run_driver(self):
        if not hasattr(self, 'is_driver_working'):
            self.is_driver_working = False

        if not self.is_driver_working:
            thread = threading.Thread(target=self.run_driver_command)
            thread.start()
        else:
            print(self.driver_process.pid)
            self.driver_process.terminate()


        self.is_driver_working = not self.is_driver_working
        self.driverBtn.setText('Отключить' if self.is_driver_working else 'Запустить')
        self.driver_status_label.setText('Работает' if self.is_driver_working else 'Отключен')

    def print_stdout(self, lines):
        for line in lines:
            print(line.strip())
    def run_driver_command(self):

        self.driver_process = subprocess.Popen(
            # 'java "-Dwebdriver.chrome.driver=d:\\work\\selenium2\\chromedriver.exe" -jar "D:\\work\\selenium2\\selenium-server-standalone-3.5.3.jar"',
           "ping google.com -n 20",
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )

        label_message = 'Отключен'
        self.driver_process.wait()
        if self.driver_process.returncode == 1:
            label_message = 'Комманда была прервана'
        self.is_driver_working = False
        print(self.driver_process.returncode)

        self.driver_status_label.setText(label_message)
        self.driverBtn.setText('Запустить')
    def run_parser(self):
        if not self.params_defined():
            return

        if not hasattr(self, 'is_parser_working'):
            self.is_parser_working = False

        if not self.is_parser_working:
            self.edit_config()
            thread = threading.Thread(target=self.run_parser_command)
            thread.start()
        else:
            self.stop_parser()

        self.is_parser_working = not self.is_parser_working

        self.parserBtn.setText('Отключить' if self.is_parser_working else 'Запустить')
        self.parser_status_label.setText('Работает' if self.is_parser_working else 'Комманда была прервана')
        self.driverBtn.setEnabled(not self.is_parser_working)

        if not hasattr(self, 'is_launcher_working') or (hasattr(self, 'is_launcher_working') and not self.is_launcher_working):
            self.launchBtn.setEnabled(not self.is_parser_working)
        else:
            self.parserBtn.setEnabled(not self.is_parser_working)
    def params_defined(self):
        if not hasattr(self, 'page') or not hasattr(self, 'selectedItem'):
            msgBox = QMessageBox()
            msgBox.setText("Выберите страницу и тип элемента")
            msgBox.exec()
            return False
        return True
    def edit_config(self):
        print(self.page)
        with open("D:\\work\\scheduler\\config.properties", "r") as config:
            content = config.read()
            params = content.split("\n")
            for i in range(len(params)):
                key_value = params[i].split(" = ")
                key = key_value[0].replace(" ", "")
                if key == "baseUrlPageNum":
                    key_value[1] = f'"https://www.chipdip.by/catalog-show/{self.selectedItem}?page={self.page}"'
                params[i] = ' = '.join(key_value)
            content = '\n'.join(params)

        with open("D:\\work\\scheduler\\config.properties", "w") as config:
            config.write(content)

    def stop_parser(self):
        subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=self.parser_process.pid))

    def run_parser_command(self):

        self.parser_process = subprocess.Popen(
            # "mvn test -Dsuite=testng",
            "ping google.com -n 20",
            # cwd='D:\\work\\microparser',
            shell=True
        )
        self.parser_process.wait()

        label_message = "Отключен"

        if self.parser_process.returncode == 1:
            label_message = "Комманда была прервана"

        self.is_parser_working = False
        print(f"парсер статус {self.parser_process.returncode}")

        self.parser_status_label.setText(label_message)
        self.parserBtn.setText('Запустить')
        self.launchBtn.setEnabled(True)
        self.parserBtn.setEnabled(True)
        self.driverBtn.setEnabled(True)

    def run_launcher(self):
        if not self.params_defined():
            return

        if not hasattr(self, 'is_launcher_working'):
            self.is_launcher_working = False

        if not self.is_launcher_working:
            thread = threading.Thread(target=self.run_listener)
            thread.start()
        else:
            self.stop_parser()
            self.parserBtn.setEnabled(True)
            self.driverBtn.setEnabled(True)
            self.is_listener_working = False

        self.is_launcher_working = not self.is_launcher_working
        self.launch_status_label.setText('Работает' if self.is_launcher_working else 'Комманда была прервана')


    def run_listener(self):
        self.delay_time_past = True
        self.hours_delay = 0
        self.is_listener_working = True
        self.launchBtn.setText('Отключить')

        while self.is_listener_working:
            if self.delay_time_past:
                if self.hours_delay != 0:
                        sleep(self.hours_delay)
                        if not self.is_listener_working:
                            break

                thread = threading.Thread(target=self.run_parser)
                thread.start()
                label_message = 'Работает'
                self.delay_time_past = False

            sleep(1)

            if self.parser_process.returncode == 0:
                self.hours_delay = random.randint(6, 10)
                label_message = f"Выполнено, выжидает интервал перед следущим запуском {self.hours_delay} часов"
                self.page = f'{int(self.page)+1}'
                self.numberLineEdit.setText(self.page)
                self.edit_config()
                self.delay_time_past = True

            elif self.parser_process.returncode != None:
                label_message = "Комманда была прервана"
                self.is_listener_working = False

            print(f"слушатель {self.parser_process.returncode}")
            self.launch_status_label.setText(label_message)

        self.launchBtn.setText('Запустить')

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
