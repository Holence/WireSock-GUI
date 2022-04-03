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
        MainWindow.resize(972, 398)
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        self.horizontalLayout = QHBoxLayout(MainWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(MainWindow)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(300, 0))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_wg_file = QLineEdit(self.groupBox_2)
        self.lineEdit_wg_file.setObjectName(u"lineEdit_wg_file")
        self.lineEdit_wg_file.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_wg_file, 1, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_wg_private_key = QLineEdit(self.groupBox_2)
        self.lineEdit_wg_private_key.setObjectName(u"lineEdit_wg_private_key")

        self.gridLayout_2.addWidget(self.lineEdit_wg_private_key, 3, 0, 1, 1)

        self.comboBox_wg = QComboBox(self.groupBox_2)
        self.comboBox_wg.setObjectName(u"comboBox_wg")

        self.gridLayout_2.addWidget(self.comboBox_wg, 5, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_wg_file = DTApplyButton(self.groupBox_2)
        self.pushButton_wg_file.setObjectName(u"pushButton_wg_file")

        self.gridLayout_2.addWidget(self.pushButton_wg_file, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(300, 0))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_sock_file = QLineEdit(self.groupBox)
        self.lineEdit_sock_file.setObjectName(u"lineEdit_sock_file")
        self.lineEdit_sock_file.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_sock_file, 1, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.pushButton_sock_file = DTApplyButton(self.groupBox)
        self.pushButton_sock_file.setObjectName(u"pushButton_sock_file")

        self.gridLayout.addWidget(self.pushButton_sock_file, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit_sock_pw = QLineEdit(self.groupBox)
        self.lineEdit_sock_pw.setObjectName(u"lineEdit_sock_pw")

        self.gridLayout.addWidget(self.lineEdit_sock_pw, 5, 0, 1, 1)

        self.lineEdit_sock_un = QLineEdit(self.groupBox)
        self.lineEdit_sock_un.setObjectName(u"lineEdit_sock_un")

        self.gridLayout.addWidget(self.lineEdit_sock_un, 3, 0, 1, 1)

        self.comboBox_sock = QComboBox(self.groupBox)
        self.comboBox_sock.setObjectName(u"comboBox_sock")

        self.gridLayout.addWidget(self.comboBox_sock, 7, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.splitter.addWidget(self.layoutWidget)
        self.groupBox_3 = QGroupBox(self.splitter)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(300, 0))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.comboBox_log = QComboBox(self.groupBox_3)
        self.comboBox_log.addItem("")
        self.comboBox_log.addItem("")
        self.comboBox_log.addItem("")
        self.comboBox_log.setObjectName(u"comboBox_log")

        self.verticalLayout_2.addWidget(self.comboBox_log)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_2.addWidget(self.label_11)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox_connection_check = QComboBox(self.groupBox_3)
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.addItem("")
        self.comboBox_connection_check.setObjectName(u"comboBox_connection_check")

        self.horizontalLayout_2.addWidget(self.comboBox_connection_check)

        self.lineEdit_connection_check = QLineEdit(self.groupBox_3)
        self.lineEdit_connection_check.setObjectName(u"lineEdit_connection_check")

        self.horizontalLayout_2.addWidget(self.lineEdit_connection_check)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.plainTextEdit_extra_conf = DTPlainTextEdit(self.groupBox_3)
        self.plainTextEdit_extra_conf.setObjectName(u"plainTextEdit_extra_conf")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_extra_conf.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_extra_conf.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.plainTextEdit_extra_conf)

        self.splitter.addWidget(self.groupBox_3)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.layoutWidget1)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy1)
        self.plainTextEdit.setMinimumSize(QSize(300, 0))
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.plainTextEdit, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_switch = QPushButton(self.layoutWidget1)
        self.pushButton_switch.setObjectName(u"pushButton_switch")

        self.verticalLayout.addWidget(self.pushButton_switch)


        self.gridLayout_3.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.splitter.addWidget(self.layoutWidget1)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(MainWindow)

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
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"WireGuard", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"WireGuard Private Key", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"WireGuard Server", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"WireGuard IP List File", None))
        self.pushButton_wg_file.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sock5", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Socks5 Server", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Socks5 Password", None))
        self.pushButton_sock_file.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Socks5 List File", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Socks5 Username", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"WireSock", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Log Level", None))
        self.comboBox_log.setItemText(0, QCoreApplication.translate("MainWindow", u"none", None))
        self.comboBox_log.setItemText(1, QCoreApplication.translate("MainWindow", u"debug", None))
        self.comboBox_log.setItemText(2, QCoreApplication.translate("MainWindow", u"all", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Connection Check Field and Default Value", None))
        self.comboBox_connection_check.setItemText(0, QCoreApplication.translate("MainWindow", u"ip", None))
        self.comboBox_connection_check.setItemText(1, QCoreApplication.translate("MainWindow", u"city", None))
        self.comboBox_connection_check.setItemText(2, QCoreApplication.translate("MainWindow", u"region", None))
        self.comboBox_connection_check.setItemText(3, QCoreApplication.translate("MainWindow", u"country", None))
        self.comboBox_connection_check.setItemText(4, QCoreApplication.translate("MainWindow", u"loc", None))
        self.comboBox_connection_check.setItemText(5, QCoreApplication.translate("MainWindow", u"org", None))
        self.comboBox_connection_check.setItemText(6, QCoreApplication.translate("MainWindow", u"timezone", None))

#if QT_CONFIG(tooltip)
        self.lineEdit_connection_check.setToolTip(QCoreApplication.translate("MainWindow", u"check info at http://ipinfo.io/json", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Extended Configuration", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Terminal", None))
        self.pushButton_switch.setText("")
    # retranslateUi

