from PyQt6 import QtCore, QtGui, QtWidgets


class Ui(object):
    def setupUi(self, MainWindow):

        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

        # виджет с номером страницы
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 241, 114))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.verticalLayout.addWidget(self.label_3,  0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.numberLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.numberLineEdit.setMaximumSize(QtCore.QSize(120, 20))


        self.verticalLayout.addWidget(self.numberLineEdit, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        # виджет с типами элементов
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 130, 241, 114))

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)

        self.label_2 = QtWidgets.QLabel(parent=self.widget_2)
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)

        self.comboBox = QtWidgets.QComboBox(parent=self.widget_2)
        self.comboBox.setMaximumSize(QtCore.QSize(120, 20))
        self.verticalLayout_2.addWidget(self.comboBox, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)

        # нижний виджет с автозапуском

        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(0, 480, 600, 121))
        self.widget_3.setMinimumSize(QtCore.QSize(600, 0))

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_3)
        self.autoLaunchBtn = QtWidgets.QPushButton(parent=self.widget_3)
        self.autoLaunchBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.verticalLayout_6.addWidget(self.autoLaunchBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        # виджет с кнопками

        self.widget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(256, 10, 334, 234))

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)

        self.widget_5 = QtWidgets.QWidget(parent=self.widget_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.label_1 = QtWidgets.QLabel(parent=self.widget_5)
        self.verticalLayout_4.addWidget(self.label_1)

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

        self.parserBtn = QtWidgets.QPushButton(parent=self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.parserBtn.setSizePolicy(sizePolicy)
        self.parserBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.verticalLayout_5.addWidget(self.parserBtn, 0, QtCore.Qt.AlignmentFlag.AlignBottom)

        self.verticalLayout_3.addWidget(self.widget_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.InitTextContent(MainWindow)
        self.InitStyleSheets(MainWindow)

    def InitTextContent(self, MainWindow):
        MainWindow.setWindowTitle("Планировщик задач")
        self.label_3.setText("Номер страницы")
        self.label_2.setText("Тип элементов")
        self.comboBox.addItem("диоды")
        self.comboBox.addItem("транзисторы")
        self.comboBox.addItem("конденсаторы")
        self.comboBox.addItem("резистры")
        self.autoLaunchBtn.setText("Запустить автоматически")
        self.label_1.setText("Chrome driver")
        self.driverBtn.setText("Запустить")
        self.label_4.setText("Parser")
        self.parserBtn.setText("Запустить")

    def InitStyleSheets(self, MainWindow):
        MainWindow.setStyleSheet("background-color:  #1F1F1F; padding_bottom: 10px;")
        self.widget.setStyleSheet("background-color: #483D8B;")
        self.label_3.setStyleSheet("color: white; font-size:26px;")
        self.numberLineEdit.setStyleSheet("color: black; background-color:white; font-size: 15px;")
        self.widget_2.setStyleSheet("background-color: #483D8B;")
        self.label_2.setStyleSheet("color: white; font-size:26px;")
        self.comboBox.setStyleSheet("background-color: white; font-size: 15px;")
        self.widget_3.setStyleSheet("background-color: #483D8B;")
        self.autoLaunchBtn.setStyleSheet("background-color: #1f1f1f; color: white; font-size: 15px; padding: 20px; border-radius: 10px;")
        self.label_1.setStyleSheet("color: white; font-size:26px;")
        self.widget_4.setStyleSheet("background-color: #483D8B;")
        self.driverBtn.setStyleSheet("background-color: #1f1f1f; color: white; font-size: 15px;")
        self.label_4.setStyleSheet("color: white; font-size:26px;")
        self.parserBtn.setStyleSheet("background-color: #1f1f1f; color: white; font-size: 15px;")













