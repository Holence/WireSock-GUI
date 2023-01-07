# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_PingTool.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PingTable import PingTable


class Ui_PingTool(object):
    def setupUi(self, PingTool):
        if not PingTool.objectName():
            PingTool.setObjectName(u"PingTool")
        PingTool.resize(944, 623)
        self.horizontalLayout = QHBoxLayout(PingTool)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(PingTool)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.tableWidget_wireguard = PingTable(self.layoutWidget)
        self.tableWidget_wireguard.setObjectName(u"tableWidget_wireguard")
        self.tableWidget_wireguard.setMinimumSize(QSize(250, 0))

        self.verticalLayout.addWidget(self.tableWidget_wireguard)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.tableWidget_socks = PingTable(self.layoutWidget)
        self.tableWidget_socks.setObjectName(u"tableWidget_socks")
        self.tableWidget_socks.setMinimumSize(QSize(250, 0))

        self.verticalLayout_2.addWidget(self.tableWidget_socks)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.tableWidget_test = PingTable(self.layoutWidget1)
        self.tableWidget_test.setObjectName(u"tableWidget_test")
        self.tableWidget_test.setMinimumSize(QSize(400, 500))

        self.verticalLayout_3.addWidget(self.tableWidget_test)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.spinBox_count = QSpinBox(self.layoutWidget1)
        self.spinBox_count.setObjectName(u"spinBox_count")
        self.spinBox_count.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_count.setMinimum(1)
        self.spinBox_count.setMaximum(100)
        self.spinBox_count.setValue(10)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBox_count)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.spinBox_timeout = QSpinBox(self.layoutWidget1)
        self.spinBox_timeout.setObjectName(u"spinBox_timeout")
        self.spinBox_timeout.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_timeout.setMinimum(1)
        self.spinBox_timeout.setMaximum(10000)
        self.spinBox_timeout.setSingleStep(50)
        self.spinBox_timeout.setValue(500)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBox_timeout)

        self.pushButton_ping = QPushButton(self.layoutWidget1)
        self.pushButton_ping.setObjectName(u"pushButton_ping")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.pushButton_ping)


        self.verticalLayout_5.addLayout(self.formLayout)

        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.plainTextEdit = QPlainTextEdit(self.layoutWidget2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.plainTextEdit)

        self.splitter.addWidget(self.layoutWidget2)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(PingTool)

        QMetaObject.connectSlotsByName(PingTool)
    # setupUi

    def retranslateUi(self, PingTool):
        PingTool.setWindowTitle(QCoreApplication.translate("PingTool", u"Form", None))
        self.label.setText(QCoreApplication.translate("PingTool", u"WireGuard Severs", None))
        self.label_2.setText(QCoreApplication.translate("PingTool", u"Socks5 Severs", None))
        self.label_3.setText(QCoreApplication.translate("PingTool", u"Test Severs", None))
        self.label_5.setText(QCoreApplication.translate("PingTool", u"Count", None))
        self.label_6.setText(QCoreApplication.translate("PingTool", u"Timeout", None))
        self.spinBox_timeout.setSuffix(QCoreApplication.translate("PingTool", u" ms", None))
        self.pushButton_ping.setText(QCoreApplication.translate("PingTool", u"Ping All", None))
        self.label_4.setText(QCoreApplication.translate("PingTool", u"Ping Result", None))
    # retranslateUi

