# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledtts.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_UntitledTTS(object):
    def setupUi(self, UntitledTTS):
        if not UntitledTTS.objectName():
            UntitledTTS.setObjectName(u"UntitledTTS")
        UntitledTTS.resize(500, 310)
        UntitledTTS.setMinimumSize(QSize(500, 310))
        UntitledTTS.setMaximumSize(QSize(500, 310))
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        UntitledTTS.setWindowIcon(icon)
        self.centralwidget = QWidget(UntitledTTS)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sayButton = QPushButton(self.centralwidget)
        self.sayButton.setObjectName(u"sayButton")
        self.sayButton.setGeometry(QRect(380, 160, 111, 141))
        self.readTextEdit = QTextEdit(self.centralwidget)
        self.readTextEdit.setObjectName(u"readTextEdit")
        self.readTextEdit.setGeometry(QRect(10, 10, 481, 141))
        self.readTextEdit.setAcceptRichText(False)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 160, 361, 142))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.label_5)

        self.outputComboBox = QComboBox(self.layoutWidget)
        self.outputComboBox.setObjectName(u"outputComboBox")

        self.horizontalLayout_4.addWidget(self.outputComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.voicesComboBox = QComboBox(self.layoutWidget)
        self.voicesComboBox.setObjectName(u"voicesComboBox")

        self.horizontalLayout_3.addWidget(self.voicesComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(41, 16777215))

        self.horizontalLayout.addWidget(self.label_3)

        self.volumeSlider = QSlider(self.layoutWidget)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(100)
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.volumeSlider)

        self.volumeLabel = QLabel(self.layoutWidget)
        self.volumeLabel.setObjectName(u"volumeLabel")
        self.volumeLabel.setMinimumSize(QSize(61, 0))
        self.volumeLabel.setMaximumSize(QSize(61, 16777215))

        self.horizontalLayout.addWidget(self.volumeLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(41, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.rateSlider = QSlider(self.layoutWidget)
        self.rateSlider.setObjectName(u"rateSlider")
        self.rateSlider.setMinimum(50)
        self.rateSlider.setMaximum(500)
        self.rateSlider.setValue(200)
        self.rateSlider.setOrientation(Qt.Horizontal)
        self.rateSlider.setInvertedAppearance(False)
        self.rateSlider.setInvertedControls(False)

        self.horizontalLayout_2.addWidget(self.rateSlider)

        self.rateLabel = QLabel(self.layoutWidget)
        self.rateLabel.setObjectName(u"rateLabel")
        self.rateLabel.setMinimumSize(QSize(61, 0))
        self.rateLabel.setMaximumSize(QSize(61, 16777215))

        self.horizontalLayout_2.addWidget(self.rateLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_5.addWidget(self.label)

        self.waitTimeSpinBox = QSpinBox(self.layoutWidget)
        self.waitTimeSpinBox.setObjectName(u"waitTimeSpinBox")
        self.waitTimeSpinBox.setMaximum(60)

        self.horizontalLayout_5.addWidget(self.waitTimeSpinBox)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.resetButton = QPushButton(self.layoutWidget)
        self.resetButton.setObjectName(u"resetButton")

        self.horizontalLayout_6.addWidget(self.resetButton)

        self.aboutButton = QPushButton(self.layoutWidget)
        self.aboutButton.setObjectName(u"aboutButton")

        self.horizontalLayout_6.addWidget(self.aboutButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        UntitledTTS.setCentralWidget(self.centralwidget)

        self.retranslateUi(UntitledTTS)

        QMetaObject.connectSlotsByName(UntitledTTS)
    # setupUi

    def retranslateUi(self, UntitledTTS):
        UntitledTTS.setWindowTitle(QCoreApplication.translate("UntitledTTS", u"Untitled TTS", None))
#if QT_CONFIG(statustip)
        self.sayButton.setStatusTip(QCoreApplication.translate("UntitledTTS", u"\u5f00\u59cb/\u505c\u6b62\u8bed\u97f3\u64ad\u653e\u3002", None))
#endif // QT_CONFIG(statustip)
        self.sayButton.setText(QCoreApplication.translate("UntitledTTS", u"\u8bf4\u8bdd", None))
#if QT_CONFIG(statustip)
        self.readTextEdit.setStatusTip(QCoreApplication.translate("UntitledTTS", u"\u8f93\u5165\u8981\u6717\u8bfb\u7684\u6587\u5b57\u3002", None))
#endif // QT_CONFIG(statustip)
        self.readTextEdit.setDocumentTitle("")
        self.readTextEdit.setMarkdown("")
        self.readTextEdit.setHtml(QCoreApplication.translate("UntitledTTS", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.readTextEdit.setPlaceholderText(QCoreApplication.translate("UntitledTTS", u"\u8f93\u5165\u8981\u6717\u8bfb\u7684\u6587\u5b57...", None))
        self.label_5.setText(QCoreApplication.translate("UntitledTTS", u"\u8f93\u51fa\u8bbe\u5907", None))
#if QT_CONFIG(statustip)
        self.outputComboBox.setStatusTip(QCoreApplication.translate("UntitledTTS", u"\u9009\u62e9\u8f93\u51fa\u97f3\u9891\u7684\u8bbe\u5907\u3002", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("UntitledTTS", u"\u4eba\u58f0", None))
#if QT_CONFIG(statustip)
        self.voicesComboBox.setStatusTip(QCoreApplication.translate("UntitledTTS", u"\u9009\u62e9\u8bed\u97f3\u7684\u58f0\u97f3\u3002", None))
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("UntitledTTS", u"\u97f3\u91cf", None))
#if QT_CONFIG(statustip)
        self.volumeSlider.setStatusTip(QCoreApplication.translate("UntitledTTS", u"\u8bbe\u7f6e\u8bed\u97f3\u7684\u97f3\u91cf\u3002", None))
#endif // QT_CONFIG(statustip)
        self.volumeLabel.setText(QCoreApplication.translate("UntitledTTS", u"100%", None))
        self.label_2.setText(QCoreApplication.translate("UntitledTTS", u"\u8bed\u901f", None))
#if QT_CONFIG(statustip)
        self.rateSlider.setStatusTip(QCoreApplication.translate("UntitledTTS", u"\u8bbe\u7f6e\u8bed\u97f3\u7684\u8bed\u901f\u3002", None))
#endif // QT_CONFIG(statustip)
        self.rateLabel.setText(QCoreApplication.translate("UntitledTTS", u"200\u5b57/min", None))
        self.label.setText(QCoreApplication.translate("UntitledTTS", u"\u8bf4\u8bdd\u524d\u7b49\u5f85", None))
#if QT_CONFIG(statustip)
        self.waitTimeSpinBox.setStatusTip(QCoreApplication.translate("UntitledTTS", u"\u5728\u64ad\u653e\u8bed\u97f3\u524d\u7b49\u5f85\u4e00\u6bb5\u65f6\u95f4\u3002", None))
#endif // QT_CONFIG(statustip)
        self.waitTimeSpinBox.setSuffix(QCoreApplication.translate("UntitledTTS", u"\u79d2", None))
        self.waitTimeSpinBox.setPrefix("")
#if QT_CONFIG(statustip)
        self.resetButton.setStatusTip(QCoreApplication.translate("UntitledTTS", u"\u91cd\u7f6e\u5bf9\u8bed\u97f3\u8fdb\u884c\u7684\u8bbe\u7f6e\u3002", None))
#endif // QT_CONFIG(statustip)
        self.resetButton.setText(QCoreApplication.translate("UntitledTTS", u"\u91cd\u7f6e\u8bbe\u7f6e", None))
#if QT_CONFIG(statustip)
        self.aboutButton.setStatusTip(QCoreApplication.translate("UntitledTTS", u"\u5173\u4e8e...", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.aboutButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.aboutButton.setText(QCoreApplication.translate("UntitledTTS", u"\u5173\u4e8e...", None))
    # retranslateUi

