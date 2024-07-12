# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Plasticframe(object):
    def setupUi(self, Plasticframe):
        if not Plasticframe.objectName():
            Plasticframe.setObjectName(u"Plasticframe")
        Plasticframe.resize(1044, 827)
        self.label = QLabel(Plasticframe)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(400, 40, 191, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(Plasticframe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(690, 130, 111, 41))
        font1 = QFont()
        font1.setPointSize(7)
        self.label_2.setFont(font1)
        self.FolderChoose = QPushButton(Plasticframe)
        self.FolderChoose.setObjectName(u"FolderChoose")
        self.FolderChoose.setGeometry(QRect(870, 280, 131, 81))
        font2 = QFont()
        font2.setPointSize(16)
        self.FolderChoose.setFont(font2)
        self.FolderChoose.setStyleSheet(u"#FolderChoose{\n"
"	background-color: rgb(208, 208, 208);\n"
"}")
        self.label_4 = QLabel(Plasticframe)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(690, 270, 120, 20))
        font3 = QFont()
        font3.setPointSize(9)
        self.label_4.setFont(font3)
        self.label_3 = QLabel(Plasticframe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 100, 151, 71))
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        self.label_3.setFont(font4)
        self.LoadPath = QTextBrowser(Plasticframe)
        self.LoadPath.setObjectName(u"LoadPath")
        self.LoadPath.setGeometry(QRect(690, 500, 301, 261))
        self.Result = QLabel(Plasticframe)
        self.Result.setObjectName(u"Result")
        self.Result.setGeometry(QRect(480, 100, 131, 71))
        self.Result.setFont(font4)
        self.Start = QPushButton(Plasticframe)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(680, 180, 131, 81))
        self.Start.setFont(font2)
        self.Start.setStyleSheet(u"#Start{\n"
"	\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        self.Stop = QPushButton(Plasticframe)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setGeometry(QRect(870, 180, 131, 81))
        self.Stop.setFont(font2)
        self.Stop.setStyleSheet(u"#Stop{\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.Result_type = QLabel(Plasticframe)
        self.Result_type.setObjectName(u"Result_type")
        self.Result_type.setGeometry(QRect(690, 300, 121, 61))
        self.Result_type.setFont(font2)
        self.Clear = QPushButton(Plasticframe)
        self.Clear.setObjectName(u"Clear")
        self.Clear.setGeometry(QRect(900, 420, 101, 51))
        self.Clear.setFont(font2)
        self.Clear.setStyleSheet(u"#FolderChoose{\n"
"	background-color: rgb(208, 208, 208);\n"
"}")
        self.label_5 = QLabel(Plasticframe)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(700, 390, 72, 15))
        self.label_6 = QLabel(Plasticframe)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(700, 420, 72, 15))
        self.label_7 = QLabel(Plasticframe)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(710, 450, 72, 15))
        self.NG = QLabel(Plasticframe)
        self.NG.setObjectName(u"NG")
        self.NG.setGeometry(QRect(790, 390, 72, 15))
        self.Pass = QLabel(Plasticframe)
        self.Pass.setObjectName(u"Pass")
        self.Pass.setGeometry(QRect(790, 420, 72, 15))
        self.Sum = QLabel(Plasticframe)
        self.Sum.setObjectName(u"Sum")
        self.Sum.setGeometry(QRect(790, 450, 72, 15))
        self.ImgShow = QLabel(Plasticframe)
        self.ImgShow.setObjectName(u"ImgShow")
        self.ImgShow.setGeometry(QRect(20, 170, 581, 591))
        self.line = QFrame(Plasticframe)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(600, 100, 41, 711))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(Plasticframe)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 90, 1051, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(Plasticframe)

        QMetaObject.connectSlotsByName(Plasticframe)
    # setupUi

    def retranslateUi(self, Plasticframe):
        Plasticframe.setWindowTitle(QCoreApplication.translate("Plasticframe", u"Plasticframe", None))
        self.label.setText(QCoreApplication.translate("Plasticframe", u"\u624b\u673a\u80f6\u6846\u7f3a\u9677\u68c0\u6d4b", None))
        self.label_2.setText("")
        self.FolderChoose.setText(QCoreApplication.translate("Plasticframe", u"\u9009\u62e9\u56fe\u50cf", None))
        self.label_4.setText(QCoreApplication.translate("Plasticframe", u"\u7f3a\u9677\u7c7b\u578b", None))
        self.label_3.setText(QCoreApplication.translate("Plasticframe", u"\u68c0\u6d4b\u7ed3\u679c\uff1a", None))
        self.Result.setText("")
        self.Start.setText(QCoreApplication.translate("Plasticframe", u"\u542f\u52a8", None))
        self.Stop.setText(QCoreApplication.translate("Plasticframe", u"\u505c\u6b62", None))
        self.Result_type.setText("")
        self.Clear.setText(QCoreApplication.translate("Plasticframe", u"\u6e05\u7a7a", None))
        self.label_5.setText(QCoreApplication.translate("Plasticframe", u"\u7f3a\u9677\u4e2a\u6570\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Plasticframe", u"\u901a\u8fc7\u4e2a\u6570\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Plasticframe", u"\u603b\u4e2a\u6570\uff1a", None))
        self.NG.setText(QCoreApplication.translate("Plasticframe", u"0", None))
        self.Pass.setText(QCoreApplication.translate("Plasticframe", u"0", None))
        self.Sum.setText(QCoreApplication.translate("Plasticframe", u"0", None))
        self.ImgShow.setText("")
    # retranslateUi

