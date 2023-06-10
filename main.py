from PyQt5 import QtCore, QtGui, QtWidgets
from extract_url import get_url
from threading import Thread
from download_part import down_song
from suggestions import Sug_Window
import sqlite3
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 66, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.sugButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sugButton.sizePolicy().hasHeightForWidth())
        self.sugButton.setSizePolicy(sizePolicy)
        self.sugButton.setMinimumSize(QtCore.QSize(60, 40))
        self.sugButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setKerning(True)
        self.sugButton.setFont(font)
        self.sugButton.setObjectName("sugButton")
        self.sugButton.clicked.connect(self.on_sug_button_click)
        self.horizontalLayout_2.addWidget(self.sugButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy)
        self.infoLabel.setMinimumSize(QtCore.QSize(0, 100))
        self.infoLabel.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.infoLabel.setFont(font)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout.addWidget(self.infoLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(18, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.searchBar = QtWidgets.QLineEdit(self.centralwidget)
        self.searchBar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy)
        self.searchBar.setMinimumSize(QtCore.QSize(0, 40))
        self.searchBar.setBaseSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.searchBar.setFont(font)
        self.searchBar.setToolTipDuration(0)
        self.searchBar.setText("")
        self.searchBar.setObjectName("searchBar")
        self.horizontalLayout.addWidget(self.searchBar)
        self.downButton = QtWidgets.QPushButton(self.centralwidget)
        self.downButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.downButton.setFont(font)
        self.downButton.setObjectName("downButton")
        self.downButton.clicked.connect(self.on_down_button_click)
        self.horizontalLayout.addWidget(self.downButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 66, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 65, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MUSIC DOWNLOADER"))
        self.sugButton.setText(_translate("MainWindow", "RECOMMEND SONGS !"))
        self.infoLabel.setText(_translate("MainWindow", "Enter the song name below and click Download"))
        self.downButton.setText(_translate("MainWindow", "Download"))
        self.label_2.setText(_translate("MainWindow", "please note that songs are stored in the same directory as this program"))

    def on_sug_button_click(self):
        conn = sqlite3.connect('songs.db')
        c = conn.cursor()

        c.execute('select * from india')
        in_list = c.fetchall()

        c.execute('select * from global')
        gb_list = c.fetchall()

        conn.close()

        self.window = QtWidgets.QMainWindow()
        self.sug_ui = Sug_Window()
        self.sug_ui.setupUi(self.window)

        for i in in_list:
            self.sug_ui.indiaTop.addItem(i[1])

        for i in gb_list:
            self.sug_ui.globalTop.addItem(i[1])

        self.window.show()


    def on_down_button_click(self):
        song_name = self.searchBar.text()
        self.downButton.setEnabled(False)
        self.label_2.setText('!!PLEASE WAIT WHILE THE SONG IS DOWNLOADING!!')
        if song_name.strip():
            l = [self.label_2,self.searchBar,self.downButton]
            thread1 = Thread(target=get_url,args=(song_name,l),daemon=True)
            thread1.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
