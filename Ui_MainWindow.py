# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DTPySide.DTWidget import DTApplyButton
from DTPySide.DTWidget import DTPlainTextEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(785, 422)
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        self.actionToggle_Connection = QAction(MainWindow)
        self.actionToggle_Connection.setObjectName(u"actionToggle_Connection")
        self.horizontalLayout = QHBoxLayout(MainWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(MainWindow)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(300, 0))
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tab_wireguard = QWidget()
        self.tab_wireguard.setObjectName(u"tab_wireguard")
        self.gridLayout = QGridLayout(self.tab_wireguard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.lineEdit_wg_file = QLineEdit(self.tab_wireguard)
        self.lineEdit_wg_file.setObjectName(u"lineEdit_wg_file")
        self.lineEdit_wg_file.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_wg_file, 1, 0, 1, 1)

        self.label_2 = QLabel(self.tab_wireguard)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_wg_private_key = QLineEdit(self.tab_wireguard)
        self.lineEdit_wg_private_key.setObjectName(u"lineEdit_wg_private_key")

        self.gridLayout.addWidget(self.lineEdit_wg_private_key, 3, 0, 1, 1)

        self.pushButton_wg_file = DTApplyButton(self.tab_wireguard)
        self.pushButton_wg_file.setObjectName(u"pushButton_wg_file")

        self.gridLayout.addWidget(self.pushButton_wg_file, 1, 1, 1, 1)

        self.label_8 = QLabel(self.tab_wireguard)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.comboBox_wg = QComboBox(self.tab_wireguard)
        self.comboBox_wg.setObjectName(u"comboBox_wg")

        self.gridLayout.addWidget(self.comboBox_wg, 5, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.tab_wireguard)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.pushButton_openwg = QPushButton(self.tab_wireguard)
        self.pushButton_openwg.setObjectName(u"pushButton_openwg")

        self.horizontalLayout_4.addWidget(self.pushButton_openwg)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_wireguard, "")
        self.tab_sock5 = QWidget()
        self.tab_sock5.setObjectName(u"tab_sock5")
        self.gridLayout_2 = QGridLayout(self.tab_sock5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, -1)
        self.label_13 = QLabel(self.tab_sock5)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)

        self.comboBox_sock = QComboBox(self.tab_sock5)
        self.comboBox_sock.setObjectName(u"comboBox_sock")

        self.gridLayout_2.addWidget(self.comboBox_sock, 10, 0, 1, 1)

        self.comboBox_nordapi = QComboBox(self.tab_sock5)
        self.comboBox_nordapi.addItem("")
        self.comboBox_nordapi.addItem("")
        self.comboBox_nordapi.addItem("")
        self.comboBox_nordapi.addItem("")
        self.comboBox_nordapi.addItem("")
        self.comboBox_nordapi.setObjectName(u"comboBox_nordapi")

        self.gridLayout_2.addWidget(self.comboBox_nordapi, 4, 0, 1, 1)

        self.pushButton_sock_file = DTApplyButton(self.tab_sock5)
        self.pushButton_sock_file.setObjectName(u"pushButton_sock_file")

        self.gridLayout_2.addWidget(self.pushButton_sock_file, 2, 1, 1, 1)

        self.pushButton_getsock = DTApplyButton(self.tab_sock5)
        self.pushButton_getsock.setObjectName(u"pushButton_getsock")

        self.gridLayout_2.addWidget(self.pushButton_getsock, 4, 1, 1, 1)

        self.label_3 = QLabel(self.tab_sock5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.lineEdit_sock_file = QLineEdit(self.tab_sock5)
        self.lineEdit_sock_file.setObjectName(u"lineEdit_sock_file")
        self.lineEdit_sock_file.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_sock_file, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 11, 0, 1, 1)

        self.label_7 = QLabel(self.tab_sock5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 9, 0, 1, 1)

        self.checkBox_sock5 = QCheckBox(self.tab_sock5)
        self.checkBox_sock5.setObjectName(u"checkBox_sock5")

        self.gridLayout_2.addWidget(self.checkBox_sock5, 0, 0, 1, 1)

        self.label_5 = QLabel(self.tab_sock5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 7, 0, 1, 1)

        self.lineEdit_sock_pw = QLineEdit(self.tab_sock5)
        self.lineEdit_sock_pw.setObjectName(u"lineEdit_sock_pw")

        self.gridLayout_2.addWidget(self.lineEdit_sock_pw, 8, 0, 1, 1)

        self.lineEdit_sock_un = QLineEdit(self.tab_sock5)
        self.lineEdit_sock_un.setObjectName(u"lineEdit_sock_un")

        self.gridLayout_2.addWidget(self.lineEdit_sock_un, 6, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.tab_sock5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.pushButton_opensock = QPushButton(self.tab_sock5)
        self.pushButton_opensock.setObjectName(u"pushButton_opensock")

        self.horizontalLayout_3.addWidget(self.pushButton_opensock)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_sock5, "")
        self.tab_wiresock = QWidget()
        self.tab_wiresock.setObjectName(u"tab_wiresock")
        self.verticalLayout_2 = QVBoxLayout(self.tab_wiresock)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.label_4 = QLabel(self.tab_wiresock)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.comboBox_log = QComboBox(self.tab_wiresock)
        self.comboBox_log.addItem("")
        self.comboBox_log.addItem("")
        self.comboBox_log.addItem("")
        self.comboBox_log.setObjectName(u"comboBox_log")

        self.verticalLayout_2.addWidget(self.comboBox_log)

        self.label_12 = QLabel(self.tab_wiresock)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12)

        self.lineEdit_extra_CMD = QLineEdit(self.tab_wiresock)
        self.lineEdit_extra_CMD.setObjectName(u"lineEdit_extra_CMD")

        self.verticalLayout_2.addWidget(self.lineEdit_extra_CMD)

        self.label_10 = QLabel(self.tab_wiresock)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.plainTextEdit_extra_conf = DTPlainTextEdit(self.tab_wiresock)
        self.plainTextEdit_extra_conf.setObjectName(u"plainTextEdit_extra_conf")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_extra_conf.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_extra_conf.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.plainTextEdit_extra_conf)

        self.tabWidget.addTab(self.tab_wiresock, "")
        self.splitter.addWidget(self.tabWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.layoutWidget1)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy1)
        self.plainTextEdit.setMinimumSize(QSize(400, 0))
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.plainTextEdit, 3, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_switch = QPushButton(self.layoutWidget1)
        self.pushButton_switch.setObjectName(u"pushButton_switch")

        self.verticalLayout.addWidget(self.pushButton_switch)


        self.gridLayout_3.addLayout(self.verticalLayout, 3, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox_connection_check = QComboBox(self.layoutWidget1)
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.setObjectName(u"comboBox_connection_check")

        self.horizontalLayout_2.addWidget(self.comboBox_connection_check)

        self.lineEdit_connection_check = QLineEdit(self.layoutWidget1)
        self.lineEdit_connection_check.setObjectName(u"lineEdit_connection_check")

        self.horizontalLayout_2.addWidget(self.lineEdit_connection_check)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)

        self.splitter.addWidget(self.layoutWidget1)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
#if QT_CONFIG(tooltip)
        self.actionUpdate.setToolTip(QCoreApplication.translate("MainWindow", u"Update", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionUpdate.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionToggle_Connection.setText(QCoreApplication.translate("MainWindow", u"Toggle Connection", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"WireGuard Private Key", None))
        self.pushButton_wg_file.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"WireGuard Server", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"WireGuard IP List File", None))
        self.pushButton_openwg.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_wireguard), QCoreApplication.translate("MainWindow", u"WireGuard", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Get Sock5 Server from Nord API", None))
        self.comboBox_nordapi.setItemText(0, QCoreApplication.translate("MainWindow", u"https://api.nordvpn.com", None))
        self.comboBox_nordapi.setItemText(1, QCoreApplication.translate("MainWindow", u"https://zwyr157wwiu6eior.com", None))
        self.comboBox_nordapi.setItemText(2, QCoreApplication.translate("MainWindow", u"https://qfvi5yhkk86d38x.xyz", None))
        self.comboBox_nordapi.setItemText(3, QCoreApplication.translate("MainWindow", u"https://nllp8upbpk2da4p.xyz", None))
        self.comboBox_nordapi.setItemText(4, QCoreApplication.translate("MainWindow", u"https://icpsuawn1zy5amys.com", None))

        self.pushButton_sock_file.setText("")
        self.pushButton_getsock.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Socks5 Username", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Socks5 Server", None))
        self.checkBox_sock5.setText(QCoreApplication.translate("MainWindow", u"Enable Sock5", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Socks5 Password", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Socks5 List File", None))
        self.pushButton_opensock.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sock5), QCoreApplication.translate("MainWindow", u"Sock5", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Log Level", None))
        self.comboBox_log.setItemText(0, QCoreApplication.translate("MainWindow", u"none", None))
        self.comboBox_log.setItemText(1, QCoreApplication.translate("MainWindow", u"debug", None))
        self.comboBox_log.setItemText(2, QCoreApplication.translate("MainWindow", u"all", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Extended CMD", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Extended Configuration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_wiresock), QCoreApplication.translate("MainWindow", u"WireSock", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("MainWindow", u"Check your original IP info at https://ipinfo.io/json and fill in the blank below.", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Connection Check", None))
        self.pushButton_switch.setText("")
        self.comboBox_connection_check.setItemText(0, QCoreApplication.translate("MainWindow", u"ip", None))
        self.comboBox_connection_check.setItemText(1, QCoreApplication.translate("MainWindow", u"city", None))
        self.comboBox_connection_check.setItemText(2, QCoreApplication.translate("MainWindow", u"region", None))
        self.comboBox_connection_check.setItemText(3, QCoreApplication.translate("MainWindow", u"country", None))
        self.comboBox_connection_check.setItemText(4, QCoreApplication.translate("MainWindow", u"loc", None))
        self.comboBox_connection_check.setItemText(5, QCoreApplication.translate("MainWindow", u"org", None))
        self.comboBox_connection_check.setItemText(6, QCoreApplication.translate("MainWindow", u"timezone", None))

#if QT_CONFIG(tooltip)
        self.comboBox_connection_check.setToolTip(QCoreApplication.translate("MainWindow", u"Check your original IP info at https://ipinfo.io/json and fill in the blank below.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_connection_check.setToolTip(QCoreApplication.translate("MainWindow", u"Check your original IP info at https://ipinfo.io/json and fill in the blank below.", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Terminal", None))
    # retranslateUi

