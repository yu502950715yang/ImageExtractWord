# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imageExtractWord.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ImageToWord(object):
    def setupUi(self, ImageToWord):
        if not ImageToWord.objectName():
            ImageToWord.setObjectName(u"ImageToWord")
        ImageToWord.resize(446, 396)
        self.verticalLayout = QVBoxLayout(ImageToWord)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(ImageToWord)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_imageType = QComboBox(ImageToWord)
        self.comboBox_imageType.addItem("")
        self.comboBox_imageType.addItem("")
        self.comboBox_imageType.setObjectName(u"comboBox_imageType")

        self.horizontalLayout.addWidget(self.comboBox_imageType)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(ImageToWord)
        self.label_2.setObjectName(u"label_2")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(255, 63, 63, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(127, 0, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(170, 0, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 128))
        brush8.setStyle(Qt.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
        # endif
        self.label_2.setPalette(palette)

        self.verticalLayout.addWidget(self.label_2)

        self.tableWidget_image = QTableWidget(ImageToWord)
        if (self.tableWidget_image.columnCount() < 3):
            self.tableWidget_image.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_image.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_image.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_image.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_image.setObjectName(u"tableWidget_image")

        self.verticalLayout.addWidget(self.tableWidget_image)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(ImageToWord)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_outPath = QLineEdit(ImageToWord)
        self.lineEdit_outPath.setObjectName(u"lineEdit_outPath")

        self.horizontalLayout_3.addWidget(self.lineEdit_outPath)

        self.pushButton_choosePath = QPushButton(ImageToWord)
        self.pushButton_choosePath.setObjectName(u"pushButton_choosePath")

        self.horizontalLayout_3.addWidget(self.pushButton_choosePath)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_imageExtract = QPushButton(ImageToWord)
        self.pushButton_imageExtract.setObjectName(u"pushButton_imageExtract")

        self.horizontalLayout_2.addWidget(self.pushButton_imageExtract)

        self.pushButton_cleanTable = QPushButton(ImageToWord)
        self.pushButton_cleanTable.setObjectName(u"pushButton_cleanTable")

        self.horizontalLayout_2.addWidget(self.pushButton_cleanTable)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ImageToWord)

        self.comboBox_imageType.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(ImageToWord)

    # setupUi

    def retranslateUi(self, ImageToWord):
        ImageToWord.setWindowTitle(QCoreApplication.translate("ImageToWord", u"\u56fe\u7247\u8f6cWord", None))
        self.label.setText(QCoreApplication.translate("ImageToWord", u"\u56fe\u7247\u7c7b\u578b\uff1a", None))
        self.comboBox_imageType.setItemText(0, QCoreApplication.translate("ImageToWord",
                                                                          u"\u529e\u516c\u6587\u6863\u56fe\u7247",
                                                                          None))
        self.comboBox_imageType.setItemText(1, QCoreApplication.translate("ImageToWord",
                                                                          u"\u624b\u5199\u6587\u5b57\u56fe\u7247",
                                                                          None))

        self.comboBox_imageType.setCurrentText(
            QCoreApplication.translate("ImageToWord", u"\u529e\u516c\u6587\u6863\u56fe\u7247", None))
        self.label_2.setText(QCoreApplication.translate("ImageToWord",
                                                        u"\u5c06\u6587\u4ef6\u62d6\u52a8\u5230\u4e0b\u9762\u7a7a\u767d\u5904",
                                                        None))
        ___qtablewidgetitem = self.tableWidget_image.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ImageToWord", u"\u6587\u4ef6\u540d", None));
        ___qtablewidgetitem1 = self.tableWidget_image.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ImageToWord", u"\u8def\u5f84", None));
        ___qtablewidgetitem2 = self.tableWidget_image.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ImageToWord", u"\u64cd\u4f5c", None));
        self.label_3.setText(
            QCoreApplication.translate("ImageToWord", u"\u751f\u6210\u6587\u4ef6\u76ee\u5f55\uff1a", None))
        self.pushButton_choosePath.setText(QCoreApplication.translate("ImageToWord", u"\u751f\u6210\u76ee\u5f55", None))
        self.pushButton_imageExtract.setText(
            QCoreApplication.translate("ImageToWord", u"\u56fe\u7247\u8f6c\u6362", None))
        self.pushButton_cleanTable.setText(QCoreApplication.translate("ImageToWord", u"\u6e05\u7a7a\u5217\u8868", None))
    # retranslateUi
