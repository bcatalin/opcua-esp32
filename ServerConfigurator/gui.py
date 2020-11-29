# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ServerConfigurator(object):
    def setupUi(self, ServerConfigurator):
        ServerConfigurator.setObjectName("ServerConfigurator")
        ServerConfigurator.resize(520, 286)
        self.centralwidget = QtWidgets.QWidget(ServerConfigurator)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 10, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.connected_device_name = QtWidgets.QTextEdit(self.centralwidget)
        self.connected_device_name.setGeometry(QtCore.QRect(150, 10, 271, 31))
        self.connected_device_name.setObjectName("connected_device_name")
        self.available_wifis = QtWidgets.QComboBox(self.centralwidget)
        self.available_wifis.setGeometry(QtCore.QRect(150, 163, 251, 21))
        self.available_wifis.setObjectName("available_wifis")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(38, 164, 94, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(38, 194, 56, 16))
        self.label_2.setObjectName("label_2")
        self.connection_type_label = QtWidgets.QLabel(self.centralwidget)
        self.connection_type_label.setGeometry(QtCore.QRect(41, 61, 101, 16))
        self.connection_type_label.setObjectName("connection_type_label")
        self.wifi_password = QtWidgets.QTextEdit(self.centralwidget)
        self.wifi_password.setGeometry(QtCore.QRect(150, 190, 256, 31))
        self.wifi_password.setObjectName("wifi_password")
        self.connection_type_combo = QtWidgets.QComboBox(self.centralwidget)
        self.connection_type_combo.setGeometry(QtCore.QRect(152, 62, 81, 21))
        self.connection_type_combo.setObjectName("connection_type_combo")
        self.connection_type_combo.addItem("")
        self.connection_type_combo.addItem("")
        self.Download = QtWidgets.QPushButton(self.centralwidget)
        self.Download.setGeometry(QtCore.QRect(428, 184, 81, 31))
        self.Download.setObjectName("Download")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 20, 101, 16))
        self.label_4.setObjectName("label_4")
        self.security_version_combo = QtWidgets.QComboBox(self.centralwidget)
        self.security_version_combo.setGeometry(QtCore.QRect(151, 101, 81, 21))
        self.security_version_combo.setObjectName("security_version_combo")
        self.security_version_combo.addItem("")
        self.security_version_combo.addItem("")
        self.security_version_label = QtWidgets.QLabel(self.centralwidget)
        self.security_version_label.setGeometry(QtCore.QRect(40, 100, 101, 16))
        self.security_version_label.setObjectName("security_version_label")
        self.pop_text = QtWidgets.QTextEdit(self.centralwidget)
        self.pop_text.setGeometry(QtCore.QRect(150, 130, 256, 21))
        self.pop_text.setObjectName("pop_text")
        self.pop_label = QtWidgets.QLabel(self.centralwidget)
        self.pop_label.setGeometry(QtCore.QRect(40, 130, 101, 16))
        self.pop_label.setObjectName("pop_label")
        ServerConfigurator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ServerConfigurator)
        self.statusbar.setObjectName("statusbar")
        ServerConfigurator.setStatusBar(self.statusbar)

        self.retranslateUi(ServerConfigurator)
        QtCore.QMetaObject.connectSlotsByName(ServerConfigurator)

    def retranslateUi(self, ServerConfigurator):
        _translate = QtCore.QCoreApplication.translate
        ServerConfigurator.setWindowTitle(_translate("ServerConfigurator", "MainWindow"))
        self.pushButton.setText(_translate("ServerConfigurator", "Connect"))
        self.label.setText(_translate("ServerConfigurator", "Available Wi-Fis"))
        self.label_2.setText(_translate("ServerConfigurator", "Password"))
        self.connection_type_label.setText(_translate("ServerConfigurator", "Connection Type"))
        self.connection_type_combo.setItemText(0, _translate("ServerConfigurator", "Ethernet"))
        self.connection_type_combo.setItemText(1, _translate("ServerConfigurator", "Wi-Fi"))
        self.Download.setText(_translate("ServerConfigurator", "Download"))
        self.label_4.setText(_translate("ServerConfigurator", "Connection Type"))
        self.security_version_combo.setItemText(0, _translate("ServerConfigurator", "0"))
        self.security_version_combo.setItemText(1, _translate("ServerConfigurator", "1"))
        self.security_version_label.setText(_translate("ServerConfigurator", "Security Version"))
        self.pop_label.setText(_translate("ServerConfigurator", "Pop"))
