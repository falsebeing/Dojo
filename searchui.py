# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(942, 735)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.card_search_widget = QWidget(self.centralwidget)
        self.card_search_widget.setObjectName(u"card_search_widget")
        self.card_search_widget.setGeometry(QRect(90, 90, 831, 431))
        self.results_tree = QTreeView(self.card_search_widget)
        self.results_tree.setObjectName(u"results_tree")
        self.results_tree.setGeometry(QRect(20, 70, 360, 351))
        self.results_tree.setSelectionBehavior(QAbstractItemView.SelectColumns)
        self.card_preview = QLabel(self.card_search_widget)
        self.card_preview.setObjectName(u"card_preview")
        self.card_preview.setGeometry(QRect(390, 0, 268, 375))
        self.card_preview.setAlignment(Qt.AlignCenter)
        self.add_card_button = QPushButton(self.card_search_widget)
        self.add_card_button.setObjectName(u"add_card_button")
        self.add_card_button.setGeometry(QRect(410, 380, 227, 45))
        self.layoutWidget = QWidget(self.card_search_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 40, 361, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.search_entry = QLineEdit(self.layoutWidget)
        self.search_entry.setObjectName(u"search_entry")

        self.horizontalLayout.addWidget(self.search_entry)

        self.search_button = QPushButton(self.layoutWidget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setEnabled(True)

        self.horizontalLayout.addWidget(self.search_button)

        self.radioButton = QRadioButton(self.card_search_widget)
        self.collection_choice = QButtonGroup(MainWindow)
        self.collection_choice.setObjectName(u"collection_choice")
        self.collection_choice.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(50, 10, 131, 21))
        self.radioButton_2 = QRadioButton(self.card_search_widget)
        self.collection_choice.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(220, 10, 101, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 942, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.card_preview.setText(QCoreApplication.translate("MainWindow", u"Card Preview", None))
#if QT_CONFIG(tooltip)
        self.add_card_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add card to active deck</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.add_card_button.setText(QCoreApplication.translate("MainWindow", u"Add Card", None))
        self.search_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search for a card...", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"&Search", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Full Card Catalog", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"My Collection", None))
    # retranslateUi

