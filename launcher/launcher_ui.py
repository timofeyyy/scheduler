from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHBoxLayout, QWidget


class LauncherUI(object):
    def setup(self, MainWindow):
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))

        self.spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

        self.leftWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.leftWidget.setGeometry(QtCore.QRect(10, 10, 241, 450))

        self.leftVerticalLayout = QtWidgets.QVBoxLayout(self.leftWidget)

        self.init_page_widget()
        self.init_site_widget()
        self.init_type_widget()
        self.init_category_widget()
        self.init_url_widget()
        self.init_interval_widget()

        self.rightWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.rightWidget.setGeometry(QtCore.QRect(256, 10, 334, 200))

        self.rightVerticalLayout = QtWidgets.QVBoxLayout(self.rightWidget)

        self.init_parser_widget()
        self.init_auto_parser_widget()

        MainWindow.setCentralWidget(self.centralwidget)

        self.init_text_content(MainWindow)
        self.init_stylesheets(MainWindow)

    def init_stylesheets(self, MainWindow):
        MainWindow.setStyleSheet("padding_bottom: 10px;")
        self.siteLabel.setStyleSheet("font-size:26px;")
        self.numberPageLabel.setStyleSheet("font-size:26px;")
        self.typeLabel.setStyleSheet("font-size:26px;")
        self.itemLabel.setStyleSheet("font-size:26px;")
        self.intervalLabel.setStyleSheet("font-size:26px;")

        self.parserLabel.setStyleSheet("font-size:26px;")
        self.autoParserLabel.setStyleSheet("font-size:26px;")

        self.numberPageLineEdit.setStyleSheet("font-size: 15px;")

        self.autoParserButton.setStyleSheet("font-size: 15px;")
        self.parserButton.setStyleSheet("font-size: 15px;")

        self.hoursFromLabel.setStyleSheet("font-size: 15px;")
        self.hoursToLabel.setStyleSheet("font-size: 15px;")




    def init_interval_widget(self):
        self.leftVerticalLayout.addItem(self.spacer)

        self.intervalLabel = QtWidgets.QLabel(parent=self.leftWidget)
        self.leftVerticalLayout.addWidget(self.intervalLabel, 0)

        self.hoursFromLabel = QtWidgets.QLabel(parent=self.leftWidget)
        self.leftVerticalLayout.addWidget(self.hoursFromLabel, 0)

        self.hoursFromLineEdit = QtWidgets.QLineEdit(parent=self.leftWidget)
        self.hoursFromLineEdit.setMaximumSize(QtCore.QSize(120, 20))
        self.leftVerticalLayout.addWidget(self.hoursFromLineEdit, 0)

        self.hoursToLabel = QtWidgets.QLabel(parent=self.leftWidget)
        self.leftVerticalLayout.addWidget(self.hoursToLabel, 0)

        self.hoursToLineEdit = QtWidgets.QLineEdit(parent=self.leftWidget)
        self.hoursToLineEdit.setMaximumSize(QtCore.QSize(120, 20))
        self.leftVerticalLayout.addWidget(self.hoursToLineEdit, 0)


    def init_page_widget(self):
        self.leftVerticalLayout.addItem(self.spacer)

        self.numberPageLabel = QtWidgets.QLabel(parent=self.leftWidget)
        self.leftVerticalLayout.addWidget(self.numberPageLabel, 0)

        self.numberPageLineEdit = QtWidgets.QLineEdit(parent=self.leftWidget)
        self.numberPageLineEdit.setMaximumSize(QtCore.QSize(120, 20))
        self.leftVerticalLayout.addWidget(self.numberPageLineEdit, 0)

    def init_site_widget(self):
        self.siteLabel = QtWidgets.QLabel(parent=self.leftWidget)

        self.leftVerticalLayout.addWidget(self.siteLabel, 0)

        self.siteComboBox = QtWidgets.QComboBox(parent=self.leftWidget)
        self.siteComboBox.setMaximumSize(QtCore.QSize(120, 20))
        self.leftVerticalLayout.addWidget(self.siteComboBox, 0)

    def init_type_widget(self):
        self.typeLabel = QtWidgets.QLabel(parent=self.leftWidget)
        self.leftVerticalLayout.addWidget(self.typeLabel, 0)

        self.typeComboBox = QtWidgets.QComboBox(parent=self.leftWidget)
        self.typeComboBox.setMaximumSize(QtCore.QSize(120, 20))
        self.leftVerticalLayout.addWidget(self.typeComboBox, 0)

    def init_category_widget(self):
        self.itemLabel = QtWidgets.QLabel(parent=self.leftWidget)
        self.leftVerticalLayout.addWidget(self.itemLabel, 0)

        self.leftVerticalLayout.addItem(self.spacer)

        self.itemComboBox = QtWidgets.QComboBox(parent=self.leftWidget)
        self.itemComboBox.setMaximumSize(QtCore.QSize(120, 20))
        self.leftVerticalLayout.addWidget(self.itemComboBox, 0)

        self.leftVerticalLayout.addItem(self.spacer)

    def init_parser_widget(self):
        self.parserLabel = QtWidgets.QLabel(parent=self.rightWidget)
        self.rightVerticalLayout.addWidget(self.parserLabel)
        self.parserStatusLabel = QtWidgets.QLabel(parent=self.rightWidget)
        self.rightVerticalLayout.addWidget(self.parserStatusLabel)

        self.parserButton = QtWidgets.QPushButton(parent=self.rightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.parserButton.setSizePolicy(sizePolicy)
        self.parserButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.rightVerticalLayout.addWidget(self.parserButton, 0, QtCore.Qt.AlignmentFlag.AlignBottom)

    def init_auto_parser_widget(self):
        self.autoParserLabel = QtWidgets.QLabel(parent=self.rightWidget)
        self.rightVerticalLayout.addWidget(self.autoParserLabel)
        self.autoParserStatusLabel = QtWidgets.QLabel(parent=self.rightWidget)
        self.autoParserStatusLabel.setWordWrap(True)
        self.rightVerticalLayout.addWidget(self.autoParserStatusLabel)

        self.autoParserButton = QtWidgets.QPushButton(parent=self.rightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.autoParserButton.setSizePolicy(sizePolicy)
        self.autoParserButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.rightVerticalLayout.addWidget(self.autoParserButton, 0, QtCore.Qt.AlignmentFlag.AlignBottom)

    def init_url_widget(self):
        self.urlLabel = QtWidgets.QLabel(parent=self.leftWidget)
        self.urlLabel.setWordWrap(True)
        self.leftVerticalLayout.addWidget(self.urlLabel)

    def init_text_content(self, MainWindow):
        MainWindow.setWindowTitle("scheduler")

        self.siteLabel.setText("Сайт")
        self.numberPageLabel.setText("Номер страницы")
        self.typeLabel.setText("Тип")
        self.itemLabel.setText("Категория")
        self.intervalLabel.setText("Интервал")
        self.hoursFromLabel.setText("Кол-во часов от")
        self.hoursToLabel.setText("Кол-во часов до")

        self.parserLabel.setText("Обычный режим")
        self.autoParserLabel.setText("Автоматический режим")

        self.parserButton.setText("Запустить")
        self.autoParserButton.setText("Запустить")

        self.parserStatusLabel.setText("Отключен")
        self.autoParserStatusLabel.setText("Отключен")