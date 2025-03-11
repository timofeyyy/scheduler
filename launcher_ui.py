from PyQt6 import QtCore, QtGui, QtWidgets


class Ui(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))

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

        MainWindow.setCentralWidget(self.centralwidget)

        self.InitTextContent(MainWindow)
        self.InitStyleSheets2(MainWindow)

    def InitStyleSheets2(self, MainWindow):
        MainWindow.setStyleSheet("padding_bottom: 10px;")
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















