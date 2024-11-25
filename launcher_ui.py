from PyQt6 import QtCore, QtGui, QtWidgets


class Ui(object):
    def setupUi(self, MainWindow):

        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))

<<<<<<< HEAD
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

        # виджет с номером страницы
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 241, 114))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.verticalLayout.addWidget(self.label_3,  0)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.numberLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.numberLineEdit.setMaximumSize(QtCore.QSize(120, 20))
        self.verticalLayout.addWidget(self.numberLineEdit, 0)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        # виджет с типами элементов
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 130, 241, 114))

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)

        self.label_2 = QtWidgets.QLabel(parent=self.widget_2)
        self.verticalLayout_2.addWidget(self.label_2, 0)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)

        self.comboBox = QtWidgets.QComboBox(parent=self.widget_2)
        self.comboBox.setMaximumSize(QtCore.QSize(120, 20))
        self.verticalLayout_2.addWidget(self.comboBox, 0)

        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)

        # виджет с кнопками

        self.widget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(256, 10, 334, 351))

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)

        self.widget_5 = QtWidgets.QWidget(parent=self.widget_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.label_1 = QtWidgets.QLabel(parent=self.widget_5)
        self.verticalLayout_4.addWidget(self.label_1)
        self.driver_status_label = QtWidgets.QLabel(parent=self.widget_5)
        self.verticalLayout_4.addWidget(self.driver_status_label)

        self.driverBtn = QtWidgets.QPushButton(parent=self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.driverBtn.setSizePolicy(sizePolicy)
        self.driverBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.verticalLayout_4.addWidget(self.driverBtn, 0, QtCore.Qt.AlignmentFlag.AlignBottom)



        self.verticalLayout_3.addWidget(self.widget_5)


        self.widget_6 = QtWidgets.QWidget(parent=self.widget_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_6)
        self.label_4 = QtWidgets.QLabel(parent=self.widget_6)
        self.verticalLayout_5.addWidget(self.label_4)
        self.parser_status_label = QtWidgets.QLabel(parent=self.widget_6)
        self.verticalLayout_5.addWidget(self.parser_status_label)

        self.parserBtn = QtWidgets.QPushButton(parent=self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.parserBtn.setSizePolicy(sizePolicy)
        self.parserBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.verticalLayout_5.addWidget(self.parserBtn, 0, QtCore.Qt.AlignmentFlag.AlignBottom)



        self.verticalLayout_3.addWidget(self.widget_6)



        self.widget_7 = QtWidgets.QWidget(parent=self.widget_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_7)
        self.label_5 = QtWidgets.QLabel(parent=self.widget_7)
        self.verticalLayout_6.addWidget(self.label_5)
        self.launch_status_label = QtWidgets.QLabel(parent=self.widget_7)
        self.launch_status_label.setWordWrap(True)
        self.verticalLayout_6.addWidget(self.launch_status_label)

        self.launchBtn = QtWidgets.QPushButton(parent=self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.launchBtn.setSizePolicy(sizePolicy)
        self.launchBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.verticalLayout_6.addWidget(self.launchBtn, 0, QtCore.Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.widget_7)

=======
        self.spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

        self.leftWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.leftWidget.setGeometry(QtCore.QRect(10, 10, 241, 300))

        self.leftVerticalLayout = QtWidgets.QVBoxLayout(self.leftWidget)

        self.NumPage()
        self.Site()
        self.Type()
        self.Item()
        self.Url()

        self.rightWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.rightWidget.setGeometry(QtCore.QRect(256, 10, 334, 300))

        self.rightVerticalLayout = QtWidgets.QVBoxLayout(self.rightWidget)

        self.Driver()
        self.Parser()
        self.AutoParser()





>>>>>>> 7a2660f (dictionary and ui update)

        MainWindow.setCentralWidget(self.centralwidget)

        self.InitTextContent(MainWindow)
        self.InitStyleSheets2(MainWindow)

    def InitStyleSheets2(self, MainWindow):
        MainWindow.setStyleSheet("padding_bottom: 10px;")
<<<<<<< HEAD
        self.label_1.setStyleSheet("font-size:26px;")
        self.label_2.setStyleSheet("font-size:26px;")
        self.label_3.setStyleSheet("font-size:26px;")
        self.label_4.setStyleSheet("font-size:26px;")
        self.label_5.setStyleSheet("font-size:26px;")
        self.numberLineEdit.setStyleSheet("font-size: 15px;")
        self.comboBox.setStyleSheet("font-size: 15px;")
        self.launchBtn.setStyleSheet("font-size: 15px;")
        self.driverBtn.setStyleSheet("font-size: 15px;")
        self.parserBtn.setStyleSheet("font-size: 15px;")

    def InitTextContent(self, MainWindow):
        elements = ["ic-chip", "ic-memory", "rezistory"]
        # can get it from DB
        MainWindow.setWindowTitle("Планировщик задач")


        for _ in elements:
            self.comboBox.addItem(_)

        self.label_1.setText("Chrome driver")
        self.label_2.setText("Тип элементов")
        self.label_3.setText("Номер страницы")
        self.label_4.setText("Parser")
        self.label_5.setText("Запускать автоматически")

        self.driverBtn.setText("Запустить")
        self.parserBtn.setText("Запустить")
        self.launchBtn.setText("Запустить")

        self.parser_status_label.setText("Отключен")
        self.driver_status_label.setText("Отключен")
        self.launch_status_label.setText("Отключен")

    def InitStyleSheets(self, MainWindow):
        MainWindow.setStyleSheet("background-color:  #1F1F1F; padding_bottom: 10px;")
        self.widget.setStyleSheet("background-color: #483D8B;")
        self.label_3.setStyleSheet("color: white; font-size:26px;")
        self.numberLineEdit.setStyleSheet("color: black; background-color:white; font-size: 15px;")
        self.widget_2.setStyleSheet("background-color: #483D8B;")
        self.label_2.setStyleSheet("color: white; font-size:26px;")
        self.comboBox.setStyleSheet("background-color: white; font-size: 15px;")
        self.widget_3.setStyleSheet("background-color: #483D8B;")
        self.label_1.setStyleSheet("color: white; font-size:26px;")
        self.widget_4.setStyleSheet("background-color: #483D8B;")
        self.driverBtn.setStyleSheet("background-color: #1f1f1f; color: white; font-size: 15px;")
        self.label_4.setStyleSheet("color: white; font-size:26px;")
        self.label_5.setStyleSheet("color: white; font-size:26px;")
        self.parserBtn.setStyleSheet("background-color: #1f1f1f; color: white; font-size: 15px;")
        self.launchBtn.setStyleSheet("background-color: #1f1f1f; color: white; font-size: 15px;")
=======
        self.siteLabel.setStyleSheet("font-size:26px;")
        self.numberPageLabel.setStyleSheet("font-size:26px;")
        self.typeLabel.setStyleSheet("font-size:26px;")
        self.itemLabel.setStyleSheet("font-size:26px;")
        
        self.driverLabel.setStyleSheet("font-size:26px;")
        self.parserLabel.setStyleSheet("font-size:26px;")
        self.autoParserLabel.setStyleSheet("font-size:26px;")

        self.numberPageLineEdit.setStyleSheet("font-size: 15px;")

        self.autoParserButton.setStyleSheet("font-size: 15px;")
        self.driverButton.setStyleSheet("font-size: 15px;")
        self.parserButton.setStyleSheet("font-size: 15px;")

    def NumPage(self):

        self.leftVerticalLayout.addItem(self.spacer)

        self.numberPageLabel = QtWidgets.QLabel(parent=self.leftWidget)
        self.leftVerticalLayout.addWidget(self.numberPageLabel, 0)

        self.numberPageLineEdit = QtWidgets.QLineEdit(parent=self.leftWidget)
        self.numberPageLineEdit.setMaximumSize(QtCore.QSize(120, 20))
        self.leftVerticalLayout.addWidget(self.numberPageLineEdit, 0)

    def Site(self):

        self.siteLabel = QtWidgets.QLabel(parent=self.leftWidget)

        self.leftVerticalLayout.addWidget(self.siteLabel, 0)
        # self.leftVerticalLayout.addItem(self.spacer)

        self.siteComboBox = QtWidgets.QComboBox(parent=self.leftWidget)
        self.siteComboBox.setMaximumSize(QtCore.QSize(120, 20))
        self.leftVerticalLayout.addWidget(self.siteComboBox, 0)
        # self.leftVerticalLayout.addItem(self.spacer)

    def Type(self):
        self.typeLabel = QtWidgets.QLabel(parent=self.leftWidget)
        self.leftVerticalLayout.addWidget(self.typeLabel, 0)

        # self.leftVerticalLayout.addItem(self.spacer)

        self.typeComboBox = QtWidgets.QComboBox(parent=self.leftWidget)
        self.typeComboBox.setMaximumSize(QtCore.QSize(120, 20))
        self.leftVerticalLayout.addWidget(self.typeComboBox, 0)

        # self.leftVerticalLayout.addItem(self.spacer)

    def Item(self):
        self.itemLabel = QtWidgets.QLabel(parent=self.leftWidget)
        self.leftVerticalLayout.addWidget(self.itemLabel, 0)

        self.leftVerticalLayout.addItem(self.spacer)

        self.itemComboBox = QtWidgets.QComboBox(parent=self.leftWidget)
        self.itemComboBox.setMaximumSize(QtCore.QSize(120, 20))
        self.leftVerticalLayout.addWidget(self.itemComboBox, 0)

        self.leftVerticalLayout.addItem(self.spacer)

    def Driver(self):
        self.driverLabel = QtWidgets.QLabel(parent=self.rightWidget)
        self.rightVerticalLayout.addWidget(self.driverLabel)
        self.driverStatusLabel = QtWidgets.QLabel(parent=self.rightWidget)
        self.rightVerticalLayout.addWidget(self.driverStatusLabel)

        self.driverButton = QtWidgets.QPushButton(parent=self.rightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.driverButton.setSizePolicy(sizePolicy)
        self.driverButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.rightVerticalLayout.addWidget(self.driverButton, 0, QtCore.Qt.AlignmentFlag.AlignBottom)

    def Parser(self):
        self.parserLabel = QtWidgets.QLabel(parent=self.rightWidget)
        self.rightVerticalLayout.addWidget(self.parserLabel)
        self.parserStatusLabel = QtWidgets.QLabel(parent=self.rightWidget)
        self.rightVerticalLayout.addWidget(self.parserStatusLabel)

        self.parserButton = QtWidgets.QPushButton(parent=self.rightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.parserButton.setSizePolicy(sizePolicy)
        self.parserButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.rightVerticalLayout.addWidget(self.parserButton, 0, QtCore.Qt.AlignmentFlag.AlignBottom)

    def AutoParser(self):
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

    def Url(self):
        self.urlLabel = QtWidgets.QLabel(parent=self.leftWidget)
        self.urlLabel.setWordWrap(True)
        self.leftVerticalLayout.addWidget(self.urlLabel)

    def InitTextContent(self, MainWindow):

        MainWindow.setWindowTitle("scheduler")


        self.siteLabel.setText("Site")
        self.numberPageLabel.setText("Page num")
        self.typeLabel.setText("Table")
        self.itemLabel.setText("Item")

        self.driverLabel.setText("Chrome driver")
        self.parserLabel.setText("Parser page")
        self.autoParserLabel.setText("Parser auto")

        self.driverButton.setText("Запустить")
        self.parserButton.setText("Запустить")
        self.autoParserButton.setText("Запустить")

        self.parserStatusLabel.setText("Отключен")
        self.driverStatusLabel.setText("Отключен")
        self.autoParserStatusLabel.setText("Отключен")


>>>>>>> 7a2660f (dictionary and ui update)













