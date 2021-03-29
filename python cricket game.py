# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EvaluateDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(911, 437)
        Dialog.setMinimumSize(QtCore.QSize(911, 437))
        Dialog.setMaximumSize(QtCore.QSize(911, 437))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IMAGES/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.BackgroundLbl = QtWidgets.QLabel(Dialog)
        self.BackgroundLbl.setGeometry(QtCore.QRect(0, 0, 911, 441))
        self.BackgroundLbl.setText("")
        self.BackgroundLbl.setPixmap(QtGui.QPixmap("IMAGES/ground3.jpg"))
        self.BackgroundLbl.setScaledContents(True)
        self.BackgroundLbl.setObjectName("BackgroundLbl")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(14, 18, 891, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.EvaluateGrid = QtWidgets.QGridLayout(self.layoutWidget)
        self.EvaluateGrid.setContentsMargins(0, 0, 0, 0)
        self.EvaluateGrid.setObjectName("EvaluateGrid")
        self.ComboLayot = QtWidgets.QHBoxLayout()
        self.ComboLayot.setObjectName("ComboLayot")
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ComboLayot.addItem(spacerItem)
        self.SelectCombo = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectCombo.sizePolicy().hasHeightForWidth())
        self.SelectCombo.setSizePolicy(sizePolicy)
        self.SelectCombo.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SelectCombo.setFont(font)
        self.SelectCombo.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.SelectCombo.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(14, 78, 255,150);")
        self.SelectCombo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.SelectCombo.setObjectName("SelectCombo")
        self.ComboLayot.addWidget(self.SelectCombo)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ComboLayot.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ComboLayot.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ComboLayot.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ComboLayot.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ComboLayot.addItem(spacerItem5)
        self.MatchCombo = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MatchCombo.sizePolicy().hasHeightForWidth())
        self.MatchCombo.setSizePolicy(sizePolicy)
        self.MatchCombo.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.MatchCombo.setFont(font)
        self.MatchCombo.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.MatchCombo.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 0, 150);")
        self.MatchCombo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.MatchCombo.setObjectName("MatchCombo")
        self.ComboLayot.addWidget(self.MatchCombo)
        spacerItem6 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ComboLayot.addItem(spacerItem6)
        self.EvaluateGrid.addLayout(self.ComboLayot, 1, 0, 1, 1)
        self.ListsGrid = QtWidgets.QGridLayout()
        self.ListsGrid.setObjectName("ListsGrid")
        self.TrophyGrid = QtWidgets.QGridLayout()
        self.TrophyGrid.setObjectName("TrophyGrid")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.TrophyGrid.addItem(spacerItem7, 5, 0, 1, 1)
        self.TrophyImgLbl = QtWidgets.QLabel(self.layoutWidget)
        self.TrophyImgLbl.setText("")
        self.TrophyImgLbl.setPixmap(QtGui.QPixmap("IMAGES/evaluate1.png"))
        self.TrophyImgLbl.setScaledContents(False)
        self.TrophyImgLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.TrophyImgLbl.setObjectName("TrophyImgLbl")
        self.TrophyGrid.addWidget(self.TrophyImgLbl, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.TrophyGrid.addItem(spacerItem8, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.TrophyGrid.addItem(spacerItem9, 3, 0, 1, 1)
        self.CalcScoreBtn = QtWidgets.QPushButton(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 162, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 135, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 72, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 162, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 135, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 72, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 162, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 135, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 72, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 108, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.CalcScoreBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(12)
        self.CalcScoreBtn.setFont(font)
        self.CalcScoreBtn.setStyleSheet("background-color: rgb(255, 1, 1);")
        self.CalcScoreBtn.setObjectName("CalcScoreBtn")
        self.TrophyGrid.addWidget(self.CalcScoreBtn, 2, 0, 1, 1)
        self.ListsGrid.addLayout(self.TrophyGrid, 1, 1, 1, 1)
        self.PlayersLbl = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PlayersLbl.setFont(font)
        self.PlayersLbl.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(14, 78, 255,150);")
        self.PlayersLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.PlayersLbl.setWordWrap(True)
        self.PlayersLbl.setObjectName("PlayersLbl")
        self.ListsGrid.addWidget(self.PlayersLbl, 0, 0, 1, 1)
        self.ScoreLbl = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ScoreLbl.setFont(font)
        self.ScoreLbl.setStyleSheet("color: rgb(255, 255,255);\n"
"background-color: rgba(255, 255, 0, 150);")
        self.ScoreLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ScoreLbl.setWordWrap(True)
        self.ScoreLbl.setObjectName("ScoreLbl")
        self.ListsGrid.addWidget(self.ScoreLbl, 0, 2, 1, 1)
        self.PlayersList = QtWidgets.QListWidget(self.layoutWidget)
        self.PlayersList.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 78, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 78, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 78, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 78, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 78, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 78, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.PlayersList.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PlayersList.setFont(font)
        self.PlayersList.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.PlayersList.setAutoFillBackground(False)
        self.PlayersList.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(14, 78, 255,150);")
        self.PlayersList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.PlayersList.setAutoScroll(False)
        self.PlayersList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.PlayersList.setProperty("showDropIndicator", False)
        self.PlayersList.setResizeMode(QtWidgets.QListView.Adjust)
        self.PlayersList.setObjectName("PlayersList")
        self.ListsGrid.addWidget(self.PlayersList, 1, 0, 2, 1)
        self.ScoreList = QtWidgets.QListWidget(self.layoutWidget)
        self.ScoreList.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ScoreList.setFont(font)
        self.ScoreList.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ScoreList.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 0, 150);")
        self.ScoreList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ScoreList.setAutoScroll(False)
        self.ScoreList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ScoreList.setProperty("showDropIndicator", False)
        self.ScoreList.setResizeMode(QtWidgets.QListView.Adjust)
        self.ScoreList.setObjectName("ScoreList")
        self.ListsGrid.addWidget(self.ScoreList, 1, 2, 2, 1)
        self.EvaluateGrid.addLayout(self.ListsGrid, 3, 0, 1, 1)
        self.SplitterLine = QtWidgets.QFrame(self.layoutWidget)
        self.SplitterLine.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.SplitterLine.setLineWidth(10)
        self.SplitterLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.SplitterLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SplitterLine.setObjectName("SplitterLine")
        self.EvaluateGrid.addWidget(self.SplitterLine, 2, 0, 1, 1)
        self.HeaderLbl = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HeaderLbl.sizePolicy().hasHeightForWidth())
        self.HeaderLbl.setSizePolicy(sizePolicy)
        self.HeaderLbl.setMinimumSize(QtCore.QSize(0, 0))
        self.HeaderLbl.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 1, 0, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 1, 0, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 1, 0, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 1, 0, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 1, 0, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 1, 0, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 1, 0, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 1, 0, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 1, 0, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.HeaderLbl.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.HeaderLbl.setFont(font)
        self.HeaderLbl.setStyleSheet("background-color: rgb(96, 1, 0, 175);")
        self.HeaderLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.HeaderLbl.setObjectName("HeaderLbl")
        self.EvaluateGrid.addWidget(self.HeaderLbl, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Fantasy Cricket"))
        self.CalcScoreBtn.setText(_translate("Dialog", "Calculate Score"))
        self.PlayersLbl.setText(_translate("Dialog", "Players"))
        self.ScoreLbl.setText(_translate("Dialog", "Points"))
        self.HeaderLbl.setText(_translate("Dialog", "Evaluate the Perfomance of Your Fantasy Cricket Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

import sqlite3
import sys
from GameWindow import *
from MessageDialog import *
from EvaluateDialog import *
from GetNameDialog import *
from Scoring import *

game_db = sqlite3.connect('cricket.db')
game_cursor = game_db.cursor()

class Game:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.showMaximized()
        try:
            self.new_selected = 0
            self.open_selected = 0
            self.exist_required= False
            self.team_name = ''
            self.team_details = None
            self.all_players = []
            self.team_players = []
            self.ui.msgDialog = QtWidgets.QDialog(self.MainWindow)
            self.ui.msgUi = Ui_MsgDialog()
            self.ui.evaluateDialog = QtWidgets.QDialog(self.MainWindow)
            self.ui.evaluateUi = Ui_Dialog()
            self.ui.getNameDialog = QtWidgets.QDialog(self.MainWindow)
            self.ui.getNameUi = Ui_GetNameDialog()
            self.ui.menu_Manage_Teams.triggered[QtWidgets.QAction].connect(self.manage)
            self.ui.BatRadio.toggled.connect(lambda: self.displayList(self.ui.AllPlayersList, self.all_players))
            self.ui.BwlRadio.toggled.connect(lambda: self.displayList(self.ui.AllPlayersList, self.all_players))
            self.ui.ArRadio.toggled.connect(lambda: self.displayList(self.ui.AllPlayersList, self.all_players))
            self.ui.WkRadio.toggled.connect(lambda: self.displayList(self.ui.AllPlayersList, self.all_players))
            self.ui.AllPlayersList.itemDoubleClicked.connect(self.addPlayers)
            self.ui.TeamPlayersList.itemDoubleClicked.connect(self.removePlayers)
        except Exception as e:
            self.exceptMsg(e, 'from method __init__')

        sys.exit(self.app.exec_())

    def manage(self,action):
        action_name = (action.text())
        if action_name == 'NEW Team':
            self.newTeam()
        elif action_name == 'OPEN Team':
            self.openTeam()
        elif action_name == 'SAVE Team':
            self.saveTeam()
        elif action_name == 'EVALUATE Team':
            self.evaluateTeam()

    def newTeam(self):
        self.disableWidgets()
        self.new_selected = 1
        self.exist_required = False
        self.getTeamName()
        
    def openTeam(self, team_name = None):
        self.disableWidgets()
        self.open_selected = 1
        self.exist_required = True
        if team_name == None:
            self.getTeamName()
        else:
            self.newOrOpenTeam(team_name)

    def saveTeam(self):
        try:
            value = self.ui.PointsUsedValueLbl.text()
            tables = ['Teams', 'Batsmen', 'Bowlers', 'AllRounders', 'WicketKeeper']
            team = [[[self.team_name, value]]]
            i = 0
            for g in self.team_players:
                group = []
                for p in g:
                    p = list(p)
                    p.insert(0, self.team_name)
                    group.append(p)
                    i+=1
                team.append(group)
            if i != 11:
                msg = """Uh..Oh! You might've forgot to add all the players for your team.
You need 11 players in your team to save it."""
                self.showMessage(msg)
                return
            if self.checkTeamExists(self.team_name):
                for t in tables:
                    query = "DELETE FROM "+ t +" WHERE Name = ? "
                    game_cursor.execute(query, (self.team_name,))
            i = 0
            for g in team:
                for p in g:
                    query = "INSERT INTO "+tables[i]+" VALUES (?,?)"
                    game_cursor.execute(query, (p[0], p[1]))
                    game_db.commit()
                i += 1
            self.openTeam(self.team_name)
        except Exception as e:
            self.exceptMsg(e, 'from method saveTeam')        

    def evaluateTeam(self):
        try:
            self.ui.evaluateUi.setupUi(self.ui.evaluateDialog)
            self.ui.evaluateUi.SelectCombo.activated.connect(self.getList)
            self.ui.evaluateUi.CalcScoreBtn.clicked.connect(self.getScores)
            self.getCombos()
            self.ui.evaluateDialog.show()
        except Exception as e:
            self.exceptMsg(e, 'from method evaluateTeam')
    
    def getTeamName(self):      #Opens the UI to enter team name
        self.ui.getNameUi.setupUi(self.ui.getNameDialog)
        self.ui.getNameUi.TeamNameLine.setFocus()
        self.ui.getNameUi.GetTeamNameButtons.accepted.connect(self.newOrOpenTeam)
        self.ui.getNameDialog.show()
        
    def disableWidgets(self):   #Disabeles required widgets
        self.ui.BatRadio.setEnabled(False)
        self.ui.BwlRadio.setEnabled(False)
        self.ui.ArRadio.setEnabled(False)
        self.ui.WkRadio.setEnabled(False)
        self.clearSelection()
        self.ui.PointsAvailValueLbl.setText('0')
        self.ui.PointsUsedValueLbl.setText('0')
        self.ui.TeamNameDisplayLbl.setText(' ')
        self.ui.AllPlayersList.setEnabled(False)
        self.ui.TeamPlayersList.setEnabled(False)

    def newOrOpenTeam(self, team_name = None):      #Performs appropriate action uponn recieving a team name
        try:
            if team_name == None:
                self.team_name = self.ui.getNameUi.TeamNameLine.text()
            else:
                self.team_name = team_name
            exists = self.checkTeamExists(self.team_name)
            if exists == self.exist_required:
                self.ui.TeamNameDisplayLbl.setText(self.team_name)
                self.enableWidgets()
                self.populateList(self.ui.AllPlayersList, self.all_players)
                if self.open_selected == 1:
                    self.populateList(self.ui.TeamPlayersList, self.team_name)
                    self.displayList(self.ui.TeamPlayersList, self.team_players)
                    self.getPlayerCounts(self.team_players)
                    self.getTeamPoints(self.team_players, self.ui.PointsUsedValueLbl)
                    self.ui.TeamPlayersList.setFocus()
                    for g in self.team_players:
                        for p in g:
                            self.updateLists(self.all_players,'', p[0])                           
                elif self.new_selected == 1:
                    self.new_selected = 0
                self.getTeamPoints(self.all_players, self.ui.PointsAvailValueLbl)
            else:
                if self.new_selected == 1:
                    msg = ("""Oh no! You've already created {} team.
    Create a new team or open {} team""".format(self.team_name,self.team_name))
                elif self.open_selected == 1:
                    msg = ("""Oh no! You might've forgot to create {} team.
    Enter a team you've already created or create a new team!!""".format(self.team_name))
                self.showMessage(msg)
        except Exception as e:
            self.exceptMsg(e, 'from method newOrOpenTeam')
        
    
    def checkTeamExists(self, team_name):       #Checks whether a team is already existing
        try:
            query = ['SELECT * FROM Teams WHERE Name = "'+team_name+'";']
            self.team_details = self.getQueryResult(query)
        except Exception as e:
            self.exceptMsg(e, 'from method checkTeamExists')
            return
        if self.team_details == [[]]:
            return False
        else:
            return True
        
    def enableWidgets(self):
        self.ui.BatRadio.setEnabled(True)
        self.ui.BwlRadio.setEnabled(True)
        self.ui.ArRadio.setEnabled(True)
        self.ui.WkRadio.setEnabled(True)
        self.ui.AllPlayersList.setEnabled(True)
        self.ui.TeamPlayersList.setEnabled(True)
        self.clearSelection()
        
    def showMessage(self, msg):         #Shows message from using message UI
        self.ui.msgUi.setupUi(self.ui.msgDialog)
        self.ui.msgUi.MessageLbl.setText(msg)
        self.ui.msgUi.OkButtonBox.setFocus()
        self.ui.msgDialog.show()

    def clearSelection(self):       #Clears selection of lists, radio buttons, teams, etc
        self.ui.RadioButtonGroup.setExclusive(False)
        self.ui.BatRadio.setChecked(False)
        self.ui.BwlRadio.setChecked(False)
        self.ui.ArRadio.setChecked(False)
        self.ui.WkRadio.setChecked(False)
        self.ui.RadioButtonGroup.setExclusive(True)
        self.ui.AllPlayersList.clear()
        self.ui.TeamPlayersList.clear()
        try:
            del self.all_players[0:10]
            del self.team_players[0:10]
        except:
            pass
        
    def exceptMsg(self, e, fn):
        msg = ("""We are sorry, something happened and we cannot create or open your team.
Please try again later or try changing the team name.
:(

Error: {} {}""".format(e, fn))
        self.showMessage(msg)        
        
    def populateList(self, list_name, team_name):
        try:
            if team_name == self.all_players:
                query = ['SELECT Player, CTG FROM Stats;']
            elif team_name == self.team_name:
                query = ['SELECT Batsman FROM Batsmen, Teams WHERE Teams.Name == Batsmen.Name AND Teams.Name = "'+team_name+'";',
                         'SELECT Bowler FROM Bowlers, Teams WHERE Teams.Name == Bowlers.Name AND Teams.Name = "'+team_name+'";',
                         'SELECT AR FROM AllRounders, Teams WHERE Teams.Name == AllRounders.Name AND Teams.Name = "'+team_name+'";',
                         'SELECT WK FROM WicketKeeper, Teams WHERE Teams.Name == WicketKeeper.Name AND Teams.Name = "'+team_name+'";']
                team_name = self.team_players
            result = self.getQueryResult(query)
            for r in result:
                team_name.append(r)
        except Exception as e:
            self.exceptMsg(e,'from method populateList')

    def getTeamPoints(self, team, lbl):
        try:
            points = getPoints(team)
            lbl.setText(str(points))
        except Exception as e:
            self.exceptMsg(e,'from method getPlayerStats')

    def getPlayerCounts(self, team):
        lbls = [self.ui.BatNoLbl, self.ui.BowNoLbl, self.ui.ArNoLbl, self.ui.WkNoLbl]
        i = 0
        for g in team:
            count = 0
            for p in g:
                count+=1
            lbls[i].setText(str(count))
            i+=1

    def displayList(self, list_name, team_name):
        try:
            list_name.clear()
            if list_name == self.ui.AllPlayersList:
                rb_group = [self.ui.BatRadio, self.ui.BwlRadio, self.ui.ArRadio, self.ui.WkRadio]
                checked_rb = None
                for rb in rb_group:
                    if rb.isChecked():
                        checked_rb = rb
                        break
                if checked_rb != None:
                    group = checked_rb.text()
                    if group == 'BOW':
                        group = 'BWL'
                    self.find(list_name, team_name, group)
            elif list_name == self.ui.TeamPlayersList:
                self.find(list_name, team_name)
        except Exception as e:
            self.exceptMsg(e,'from method displayList')             

    def find(self, list_name, team_name, group = ''):
        try:   
            for g in team_name:
                for p in g:
                    if group == '':
                        list_name.addItem(p[0])
                    elif group == p[1]:
                        if self.open_selected == 0:
                            list_name.addItem(p[0])
                        elif self.checkPlayerInTeam(p[0]) == 0:
                            list_name.addItem(p[0])
        except Exception as e:
            self.exceptMsg(e,'from method find')

    def getGroup(self, player):
        query = 'SELECT CTG FROM Stats Where Player = ?;'
        game_cursor.execute(query, (player,))
        group = []
        group.append(game_cursor.fetchone())
        if group[0][0] == 'BAT':
            group.append('batsmen')
            group.append(1)
        elif group[0][0] == 'BWL':
            group.append('bowlers')
            group.append(2)
        elif group[0][0] == 'AR':
            group.append('all- rounders')
            group.append(3)
        else:
            group.append('wicket keeper')
            group.append(4)
        return group

    def checkPlayerInTeam(self, player):
        for g in self.team_players:
            for p in g:
                if p[0] == player:
                    return 1
        return 0

    def addPlayers(self):
        try:
            if self.team_players == []:
                self.team_players = [ [], [], [], [] ]
            player = (self.ui.AllPlayersList.currentItem()).text()
            group = self.getGroup(player)
            group_count =  self.getGroupCount(group[0][0])
            if self.checkAddPermissible(group[0][0], group_count):
                no = 0
                for g in self.team_players:
                    no += 1
                    if no == group[2]:
                        g.append((player,))
                        break
                self.updateLists(self.all_players, self.ui.AllPlayersList)
                self.ui.TeamPlayersList.addItem(player)
            else:
                msg = """Oh no!
You can surely have more power in your team if your team has more members,
but you cannot add more than {} {}.""".format(group_count, group[1])
                self.showMessage(msg)
        except Exception as e:
            self.exceptMsg(e,'from method addPlayers')

    def removePlayers(self):
        try:
            player = (self.ui.TeamPlayersList.currentItem()).text()
            group = self.getGroup(player)
            p_details = (player, group[0][0])
            already_in_list = False
            for g in self.all_players:
                for p in g:
                    if p == p_details:
                        already_in_list = True
                        break
                if already_in_list == False:
                    g.append(p_details)
            self.updateLists(self.team_players, self.ui.TeamPlayersList)
        except Exception as e:
            self.exceptMsg(e,'from method removePlayers')

    def getGroupCount(self, group):
        if group == 'BAT':
            lbl = self.ui.BatNoLbl
        elif group == 'BWL':
            lbl = self.ui.BowNoLbl
        elif group == 'AR':
            lbl = self.ui.ArNoLbl
        else:
            lbl = self.ui.WkNoLbl
        return int(lbl.text())

    def checkAddPermissible(self, group, count):
        if (group == 'BAT' and count < 4) or ((group == 'BWL' or group == 'AR') and count < 3) or (group == 'WK' and count < 1):
            return True
        else:
            return False

    def updateLists(self, team, list_name = '', player = ''):
        if player == '':
            player = (list_name.currentItem()).text()
        for g in team:
            for p in g:
                if p[0] == player:
                    g.remove(p)
                    break
        if list_name != '':
            list_name.takeItem(list_name.currentRow())
        self.displayList(self.ui.AllPlayersList, self.all_players)
        self.getTeamPoints(self.all_players, self.ui.PointsAvailValueLbl)
        self.getTeamPoints(self.team_players, self.ui.PointsUsedValueLbl)
        self.getPlayerCounts(self.team_players)

    def getQueryResult(self, query):
        try:
            result=[]
            for q in query:
                game_cursor.execute(q)
                result.append(game_cursor.fetchall())
            return result
        except Exception as e:
            self.exceptMsg(e, 'from method getQueryResult')

##SETTINGS FOR EVALUATE DIALOG
            
    def getCombos(self):
        query = ['SELECT name FROM Teams', 'SELECT MatchID FROM AllMatches']
        result = self.getQueryResult(query)
        combo = [self.ui.evaluateUi.SelectCombo, self.ui.evaluateUi.MatchCombo]
        for c in combo:
            c.clear()
        i = 0
        for r in result:
            for item in r:
                combo[i].addItem(item[0])
            i+=1

    def getList(self):
        try:
            team_name = self.ui.evaluateUi.SelectCombo.currentText()
            list_name = self.ui.evaluateUi.PlayersList
            query = ['SELECT Batsman FROM Batsmen, Teams WHERE Teams.Name == Batsmen.Name AND Teams.Name = "'+team_name+'";',
                     'SELECT Bowler FROM Bowlers, Teams WHERE Teams.Name == Bowlers.Name AND Teams.Name = "'+team_name+'";',
                     'SELECT AR FROM AllRounders, Teams WHERE Teams.Name == AllRounders.Name AND Teams.Name = "'+team_name+'";',
                     'SELECT WK FROM WicketKeeper, Teams WHERE Teams.Name == WicketKeeper.Name AND Teams.Name = "'+team_name+'";']
            result  = self.getQueryResult(query)
            list_name.clear()
            for g in result:
                for p in g:
                    list_name.addItem(p[0])
        except Exception as e:
            self.exceptMsg(e, 'from method getList')

    def getScores(self):
        try:
            selected_match = self.ui.evaluateUi.MatchCombo.currentText()
            team_name = self.ui.evaluateUi.SelectCombo.currentText()
            list_name = self.ui.evaluateUi.ScoreList
            scores = getTeamScore(selected_match, team_name)
            list_name.clear()
            tot_score_text = ('Overall Score: {}'.format(scores[0]))
            self.ui.evaluateUi.ScoreLbl.setText(tot_score_text)
            scores.pop(0)
            for s in scores:
                list_name.addItem(str(s))
        except Exception as e:
            self.exceptMsg(e, 'from method getScores')
game1 = Game()
import sqlite3
import sys
from GameWindow import *
from MessageDialog import *
from EvaluateDialog import *
from GetNameDialog import *
from Scoring import *

game_db = sqlite3.connect('cricket.db')
game_cursor = game_db.cursor()

class Game:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.showMaximized()
        try:
            self.new_selected = 0
            self.open_selected = 0
            self.exist_required= False
            self.team_name = ''
            self.team_details = None
            self.all_players = []
            self.team_players = []
            self.ui.msgDialog = QtWidgets.QDialog(self.MainWindow)
            self.ui.msgUi = Ui_MsgDialog()
            self.ui.evaluateDialog = QtWidgets.QDialog(self.MainWindow)
            self.ui.evaluateUi = Ui_Dialog()
            self.ui.getNameDialog = QtWidgets.QDialog(self.MainWindow)
            self.ui.getNameUi = Ui_GetNameDialog()
            self.ui.menu_Manage_Teams.triggered[QtWidgets.QAction].connect(self.manage)
            self.ui.BatRadio.toggled.connect(lambda: self.displayList(self.ui.AllPlayersList, self.all_players))
            self.ui.BwlRadio.toggled.connect(lambda: self.displayList(self.ui.AllPlayersList, self.all_players))
            self.ui.ArRadio.toggled.connect(lambda: self.displayList(self.ui.AllPlayersList, self.all_players))
            self.ui.WkRadio.toggled.connect(lambda: self.displayList(self.ui.AllPlayersList, self.all_players))
            self.ui.AllPlayersList.itemDoubleClicked.connect(self.addPlayers)
            self.ui.TeamPlayersList.itemDoubleClicked.connect(self.removePlayers)
        except Exception as e:
            self.exceptMsg(e, 'from method __init__')

        sys.exit(self.app.exec_())

    def manage(self,action):
        action_name = (action.text())
        if action_name == 'NEW Team':
            self.newTeam()
        elif action_name == 'OPEN Team':
            self.openTeam()
        elif action_name == 'SAVE Team':
            self.saveTeam()
        elif action_name == 'EVALUATE Team':
            self.evaluateTeam()

    def newTeam(self):
        self.disableWidgets()
        self.new_selected = 1
        self.exist_required = False
        self.getTeamName()
        
    def openTeam(self, team_name = None):
        self.disableWidgets()
        self.open_selected = 1
        self.exist_required = True
        if team_name == None:
            self.getTeamName()
        else:
            self.newOrOpenTeam(team_name)

    def saveTeam(self):
        try:
            value = self.ui.PointsUsedValueLbl.text()
            tables = ['Teams', 'Batsmen', 'Bowlers', 'AllRounders', 'WicketKeeper']
            team = [[[self.team_name, value]]]
            i = 0
            for g in self.team_players:
                group = []
                for p in g:
                    p = list(p)
                    p.insert(0, self.team_name)
                    group.append(p)
                    i+=1
                team.append(group)
            if i != 11:
                msg = """Uh..Oh! You might've forgot to add all the players for your team.
You need 11 players in your team to save it."""
                self.showMessage(msg)
                return
            if self.checkTeamExists(self.team_name):
                for t in tables:
                    query = "DELETE FROM "+ t +" WHERE Name = ? "
                    game_cursor.execute(query, (self.team_name,))
            i = 0
            for g in team:
                for p in g:
                    query = "INSERT INTO "+tables[i]+" VALUES (?,?)"
                    game_cursor.execute(query, (p[0], p[1]))
                    game_db.commit()
                i += 1
            self.openTeam(self.team_name)
        except Exception as e:
            self.exceptMsg(e, 'from method saveTeam')        

    def evaluateTeam(self):
        try:
            self.ui.evaluateUi.setupUi(self.ui.evaluateDialog)
            self.ui.evaluateUi.SelectCombo.activated.connect(self.getList)
            self.ui.evaluateUi.CalcScoreBtn.clicked.connect(self.getScores)
            self.getCombos()
            self.ui.evaluateDialog.show()
        except Exception as e:
            self.exceptMsg(e, 'from method evaluateTeam')
    
    def getTeamName(self):      #Opens the UI to enter team name
        self.ui.getNameUi.setupUi(self.ui.getNameDialog)
        self.ui.getNameUi.TeamNameLine.setFocus()
        self.ui.getNameUi.GetTeamNameButtons.accepted.connect(self.newOrOpenTeam)
        self.ui.getNameDialog.show()
        
    def disableWidgets(self):   #Disabeles required widgets
        self.ui.BatRadio.setEnabled(False)
        self.ui.BwlRadio.setEnabled(False)
        self.ui.ArRadio.setEnabled(False)
        self.ui.WkRadio.setEnabled(False)
        self.clearSelection()
        self.ui.PointsAvailValueLbl.setText('0')
        self.ui.PointsUsedValueLbl.setText('0')
        self.ui.TeamNameDisplayLbl.setText(' ')
        self.ui.AllPlayersList.setEnabled(False)
        self.ui.TeamPlayersList.setEnabled(False)

    def newOrOpenTeam(self, team_name = None):      #Performs appropriate action uponn recieving a team name
        try:
            if team_name == None:
                self.team_name = self.ui.getNameUi.TeamNameLine.text()
            else:
                self.team_name = team_name
            exists = self.checkTeamExists(self.team_name)
            if exists == self.exist_required:
                self.ui.TeamNameDisplayLbl.setText(self.team_name)
                self.enableWidgets()
                self.populateList(self.ui.AllPlayersList, self.all_players)
                if self.open_selected == 1:
                    self.populateList(self.ui.TeamPlayersList, self.team_name)
                    self.displayList(self.ui.TeamPlayersList, self.team_players)
                    self.getPlayerCounts(self.team_players)
                    self.getTeamPoints(self.team_players, self.ui.PointsUsedValueLbl)
                    self.ui.TeamPlayersList.setFocus()
                    for g in self.team_players:
                        for p in g:
                            self.updateLists(self.all_players,'', p[0])                           
                elif self.new_selected == 1:
                    self.new_selected = 0
                self.getTeamPoints(self.all_players, self.ui.PointsAvailValueLbl)
            else:
                if self.new_selected == 1:
                    msg = ("""Oh no! You've already created {} team.
    Create a new team or open {} team""".format(self.team_name,self.team_name))
                elif self.open_selected == 1:
                    msg = ("""Oh no! You might've forgot to create {} team.
    Enter a team you've already created or create a new team!!""".format(self.team_name))
                self.showMessage(msg)
        except Exception as e:
            self.exceptMsg(e, 'from method newOrOpenTeam')
        
    
    def checkTeamExists(self, team_name):       #Checks whether a team is already existing
        try:
            query = ['SELECT * FROM Teams WHERE Name = "'+team_name+'";']
            self.team_details = self.getQueryResult(query)
        except Exception as e:
            self.exceptMsg(e, 'from method checkTeamExists')
            return
        if self.team_details == [[]]:
            return False
        else:
            return True
        
    def enableWidgets(self):
        self.ui.BatRadio.setEnabled(True)
        self.ui.BwlRadio.setEnabled(True)
        self.ui.ArRadio.setEnabled(True)
        self.ui.WkRadio.setEnabled(True)
        self.ui.AllPlayersList.setEnabled(True)
        self.ui.TeamPlayersList.setEnabled(True)
        self.clearSelection()
        
    def showMessage(self, msg):         #Shows message from using message UI
        self.ui.msgUi.setupUi(self.ui.msgDialog)
        self.ui.msgUi.MessageLbl.setText(msg)
        self.ui.msgUi.OkButtonBox.setFocus()
        self.ui.msgDialog.show()

    def clearSelection(self):       #Clears selection of lists, radio buttons, teams, etc
        self.ui.RadioButtonGroup.setExclusive(False)
        self.ui.BatRadio.setChecked(False)
        self.ui.BwlRadio.setChecked(False)
        self.ui.ArRadio.setChecked(False)
        self.ui.WkRadio.setChecked(False)
        self.ui.RadioButtonGroup.setExclusive(True)
        self.ui.AllPlayersList.clear()
        self.ui.TeamPlayersList.clear()
        try:
            del self.all_players[0:10]
            del self.team_players[0:10]
        except:
            pass
        
    def exceptMsg(self, e, fn):
        msg = ("""We are sorry, something happened and we cannot create or open your team.
Please try again later or try changing the team name.
:(

Error: {} {}""".format(e, fn))
        self.showMessage(msg)        
        
    def populateList(self, list_name, team_name):
        try:
            if team_name == self.all_players:
                query = ['SELECT Player, CTG FROM Stats;']
            elif team_name == self.team_name:
                query = ['SELECT Batsman FROM Batsmen, Teams WHERE Teams.Name == Batsmen.Name AND Teams.Name = "'+team_name+'";',
                         'SELECT Bowler FROM Bowlers, Teams WHERE Teams.Name == Bowlers.Name AND Teams.Name = "'+team_name+'";',
                         'SELECT AR FROM AllRounders, Teams WHERE Teams.Name == AllRounders.Name AND Teams.Name = "'+team_name+'";',
                         'SELECT WK FROM WicketKeeper, Teams WHERE Teams.Name == WicketKeeper.Name AND Teams.Name = "'+team_name+'";']
                team_name = self.team_players
            result = self.getQueryResult(query)
            for r in result:
                team_name.append(r)
        except Exception as e:
            self.exceptMsg(e,'from method populateList')

    def getTeamPoints(self, team, lbl):
        try:
            points = getPoints(team)
            lbl.setText(str(points))
        except Exception as e:
            self.exceptMsg(e,'from method getPlayerStats')

    def getPlayerCounts(self, team):
        lbls = [self.ui.BatNoLbl, self.ui.BowNoLbl, self.ui.ArNoLbl, self.ui.WkNoLbl]
        i = 0
        for g in team:
            count = 0
            for p in g:
                count+=1
            lbls[i].setText(str(count))
            i+=1

    def displayList(self, list_name, team_name):
        try:
            list_name.clear()
            if list_name == self.ui.AllPlayersList:
                rb_group = [self.ui.BatRadio, self.ui.BwlRadio, self.ui.ArRadio, self.ui.WkRadio]
                checked_rb = None
                for rb in rb_group:
                    if rb.isChecked():
                        checked_rb = rb
                        break
                if checked_rb != None:
                    group = checked_rb.text()
                    if group == 'BOW':
                        group = 'BWL'
                    self.find(list_name, team_name, group)
            elif list_name == self.ui.TeamPlayersList:
                self.find(list_name, team_name)
        except Exception as e:
            self.exceptMsg(e,'from method displayList')             

    def find(self, list_name, team_name, group = ''):
        try:   
            for g in team_name:
                for p in g:
                    if group == '':
                        list_name.addItem(p[0])
                    elif group == p[1]:
                        if self.open_selected == 0:
                            list_name.addItem(p[0])
                        elif self.checkPlayerInTeam(p[0]) == 0:
                            list_name.addItem(p[0])
        except Exception as e:
            self.exceptMsg(e,'from method find')

    def getGroup(self, player):
        query = 'SELECT CTG FROM Stats Where Player = ?;'
        game_cursor.execute(query, (player,))
        group = []
        group.append(game_cursor.fetchone())
        if group[0][0] == 'BAT':
            group.append('batsmen')
            group.append(1)
        elif group[0][0] == 'BWL':
            group.append('bowlers')
            group.append(2)
        elif group[0][0] == 'AR':
            group.append('all- rounders')
            group.append(3)
        else:
            group.append('wicket keeper')
            group.append(4)
        return group

    def checkPlayerInTeam(self, player):
        for g in self.team_players:
            for p in g:
                if p[0] == player:
                    return 1
        return 0

    def addPlayers(self):
        try:
            if self.team_players == []:
                self.team_players = [ [], [], [], [] ]
            player = (self.ui.AllPlayersList.currentItem()).text()
            group = self.getGroup(player)
            group_count =  self.getGroupCount(group[0][0])
            if self.checkAddPermissible(group[0][0], group_count):
                no = 0
                for g in self.team_players:
                    no += 1
                    if no == group[2]:
                        g.append((player,))
                        break
                self.updateLists(self.all_players, self.ui.AllPlayersList)
                self.ui.TeamPlayersList.addItem(player)
            else:
                msg = """Oh no!
You can surely have more power in your team if your team has more members,
but you cannot add more than {} {}.""".format(group_count, group[1])
                self.showMessage(msg)
        except Exception as e:
            self.exceptMsg(e,'from method addPlayers')

    def removePlayers(self):
        try:
            player = (self.ui.TeamPlayersList.currentItem()).text()
            group = self.getGroup(player)
            p_details = (player, group[0][0])
            already_in_list = False
            for g in self.all_players:
                for p in g:
                    if p == p_details:
                        already_in_list = True
                        break
                if already_in_list == False:
                    g.append(p_details)
            self.updateLists(self.team_players, self.ui.TeamPlayersList)
        except Exception as e:
            self.exceptMsg(e,'from method removePlayers')

    def getGroupCount(self, group):
        if group == 'BAT':
            lbl = self.ui.BatNoLbl
        elif group == 'BWL':
            lbl = self.ui.BowNoLbl
        elif group == 'AR':
            lbl = self.ui.ArNoLbl
        else:
            lbl = self.ui.WkNoLbl
        return int(lbl.text())

    def checkAddPermissible(self, group, count):
        if (group == 'BAT' and count < 4) or ((group == 'BWL' or group == 'AR') and count < 3) or (group == 'WK' and count < 1):
            return True
        else:
            return False

    def updateLists(self, team, list_name = '', player = ''):
        if player == '':
            player = (list_name.currentItem()).text()
        for g in team:
            for p in g:
                if p[0] == player:
                    g.remove(p)
                    break
        if list_name != '':
            list_name.takeItem(list_name.currentRow())
        self.displayList(self.ui.AllPlayersList, self.all_players)
        self.getTeamPoints(self.all_players, self.ui.PointsAvailValueLbl)
        self.getTeamPoints(self.team_players, self.ui.PointsUsedValueLbl)
        self.getPlayerCounts(self.team_players)

    def getQueryResult(self, query):
        try:
            result=[]
            for q in query:
                game_cursor.execute(q)
                result.append(game_cursor.fetchall())
            return result
        except Exception as e:
            self.exceptMsg(e, 'from method getQueryResult')

##SETTINGS FOR EVALUATE DIALOG
            
    def getCombos(self):
        query = ['SELECT name FROM Teams', 'SELECT MatchID FROM AllMatches']
        result = self.getQueryResult(query)
        combo = [self.ui.evaluateUi.SelectCombo, self.ui.evaluateUi.MatchCombo]
        for c in combo:
            c.clear()
        i = 0
        for r in result:
            for item in r:
                combo[i].addItem(item[0])
            i+=1

    def getList(self):
        try:
            team_name = self.ui.evaluateUi.SelectCombo.currentText()
            list_name = self.ui.evaluateUi.PlayersList
            query = ['SELECT Batsman FROM Batsmen, Teams WHERE Teams.Name == Batsmen.Name AND Teams.Name = "'+team_name+'";',
                     'SELECT Bowler FROM Bowlers, Teams WHERE Teams.Name == Bowlers.Name AND Teams.Name = "'+team_name+'";',
                     'SELECT AR FROM AllRounders, Teams WHERE Teams.Name == AllRounders.Name AND Teams.Name = "'+team_name+'";',
                     'SELECT WK FROM WicketKeeper, Teams WHERE Teams.Name == WicketKeeper.Name AND Teams.Name = "'+team_name+'";']
            result  = self.getQueryResult(query)
            list_name.clear()
            for g in result:
                for p in g:
                    list_name.addItem(p[0])
        except Exception as e:
            self.exceptMsg(e, 'from method getList')

    def getScores(self):
        try:
            selected_match = self.ui.evaluateUi.MatchCombo.currentText()
            team_name = self.ui.evaluateUi.SelectCombo.currentText()
            list_name = self.ui.evaluateUi.ScoreList
            scores = getTeamScore(selected_match, team_name)
            list_name.clear()
            tot_score_text = ('Overall Score: {}'.format(scores[0]))
            self.ui.evaluateUi.ScoreLbl.setText(tot_score_text)
            scores.pop(0)
            for s in scores:
                list_name.addItem(str(s))
        except Exception as e:
            self.exceptMsg(e, 'from method getScores')
game1 = Game()
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GameWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1373, 658)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 109, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 164, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 136, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 72, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 109, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 109, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 164, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 136, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 72, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 109, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 109, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 164, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 136, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 72, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 54, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 109, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 109, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 109, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IMAGES/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.98)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(16)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.BackgroundWidget = QtWidgets.QWidget()
        self.BackgroundWidget.setObjectName("BackgroundWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.BackgroundWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.BackgroundImgLbl = QtWidgets.QLabel(self.BackgroundWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackgroundImgLbl.sizePolicy().hasHeightForWidth())
        self.BackgroundImgLbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setWeight(75)
        self.BackgroundImgLbl.setFont(font)
        self.BackgroundImgLbl.setText("")
        self.BackgroundImgLbl.setPixmap(QtGui.QPixmap("IMAGES/ground1.jpg"))
        self.BackgroundImgLbl.setScaledContents(True)
        self.BackgroundImgLbl.setObjectName("BackgroundImgLbl")
        self.gridLayout.addWidget(self.BackgroundImgLbl, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.BackgroundWidget)
        self.widget = QtWidgets.QWidget()
        self.widget.setEnabled(False)
        self.widget.setObjectName("widget")
        self.stackedWidget.addWidget(self.widget)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 3, 2)
        self.PlayersFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayersFrame.sizePolicy().hasHeightForWidth())
        self.PlayersFrame.setSizePolicy(sizePolicy)
        self.PlayersFrame.setMinimumSize(QtCore.QSize(635, 257))
        self.PlayersFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PlayersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PlayersFrame.setObjectName("PlayersFrame")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.PlayersFrame)
        self.gridLayout_9.setContentsMargins(0, 0, 18, 18)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.PlayerFrameGrid = QtWidgets.QGridLayout()
        self.PlayerFrameGrid.setObjectName("PlayerFrameGrid")
        self.AvailPlayersGrid = QtWidgets.QGridLayout()
        self.AvailPlayersGrid.setObjectName("AvailPlayersGrid")
        self.PointsAvailGrid = QtWidgets.QGridLayout()
        self.PointsAvailGrid.setObjectName("PointsAvailGrid")
        self.PointsAvailLbl = QtWidgets.QLabel(self.PlayersFrame)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.PointsAvailLbl.setFont(font)
        self.PointsAvailLbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.PointsAvailLbl.setObjectName("PointsAvailLbl")
        self.PointsAvailGrid.addWidget(self.PointsAvailLbl, 0, 0, 1, 1)
        self.PointsAvailValueLbl = QtWidgets.QLabel(self.PlayersFrame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PointsAvailValueLbl.setFont(font)
        self.PointsAvailValueLbl.setObjectName("PointsAvailValueLbl")
        self.PointsAvailGrid.addWidget(self.PointsAvailValueLbl, 0, 1, 1, 1)
        self.AvailPlayersGrid.addLayout(self.PointsAvailGrid, 0, 0, 1, 1)
        self.SelectPlayersFrame = QtWidgets.QFrame(self.PlayersFrame)
        self.SelectPlayersFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.SelectPlayersFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SelectPlayersFrame.setObjectName("SelectPlayersFrame")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.SelectPlayersFrame)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.SelectPlayersGrid = QtWidgets.QGridLayout()
        self.SelectPlayersGrid.setObjectName("SelectPlayersGrid")
        self.AllPlayersList = QtWidgets.QListWidget(self.SelectPlayersFrame)
        self.AllPlayersList.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 77, 5, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 77, 5, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 77, 5, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 77, 5, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 77, 5, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 77, 5, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.AllPlayersList.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.AllPlayersList.setFont(font)
        self.AllPlayersList.setStyleSheet("background-color: rgb(255, 77, 5,240);\n"
"color: rgb(255, 255, 255);")
        self.AllPlayersList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.AllPlayersList.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.AllPlayersList.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.AllPlayersList.setProperty("isWrapping", False)
        self.AllPlayersList.setResizeMode(QtWidgets.QListView.Adjust)
        self.AllPlayersList.setWordWrap(True)
        self.AllPlayersList.setObjectName("AllPlayersList")
        self.SelectPlayersGrid.addWidget(self.AllPlayersList, 9, 0, 1, 1)
        self.SelectPlayersRadioGrid = QtWidgets.QGridLayout()
        self.SelectPlayersRadioGrid.setContentsMargins(-1, 0, -1, -1)
        self.SelectPlayersRadioGrid.setObjectName("SelectPlayersRadioGrid")
        self.BatRadio = QtWidgets.QRadioButton(self.SelectPlayersFrame)
        self.BatRadio.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.BatRadio.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BatRadio.setFont(font)
        self.BatRadio.setObjectName("BatRadio")
        self.RadioButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.RadioButtonGroup.setObjectName("RadioButtonGroup")
        self.RadioButtonGroup.addButton(self.BatRadio)
        self.SelectPlayersRadioGrid.addWidget(self.BatRadio, 0, 0, 1, 1)
        self.BwlRadio = QtWidgets.QRadioButton(self.SelectPlayersFrame)
        self.BwlRadio.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.BwlRadio.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BwlRadio.setFont(font)
        self.BwlRadio.setObjectName("BwlRadio")
        self.RadioButtonGroup.addButton(self.BwlRadio)
        self.SelectPlayersRadioGrid.addWidget(self.BwlRadio, 0, 1, 1, 1)
        self.ArRadio = QtWidgets.QRadioButton(self.SelectPlayersFrame)
        self.ArRadio.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.ArRadio.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ArRadio.setFont(font)
        self.ArRadio.setObjectName("ArRadio")
        self.RadioButtonGroup.addButton(self.ArRadio)
        self.SelectPlayersRadioGrid.addWidget(self.ArRadio, 0, 2, 1, 1)
        self.WkRadio = QtWidgets.QRadioButton(self.SelectPlayersFrame)
        self.WkRadio.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.WkRadio.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WkRadio.setFont(font)
        self.WkRadio.setObjectName("WkRadio")
        self.RadioButtonGroup.addButton(self.WkRadio)
        self.SelectPlayersRadioGrid.addWidget(self.WkRadio, 0, 3, 1, 1)
        self.SelectPlayersGrid.addLayout(self.SelectPlayersRadioGrid, 2, 0, 1, 1)
        self.gridLayout_11.addLayout(self.SelectPlayersGrid, 0, 0, 1, 1)
        self.AvailPlayersGrid.addWidget(self.SelectPlayersFrame, 1, 0, 1, 1)
        self.PlayerFrameGrid.addLayout(self.AvailPlayersGrid, 0, 0, 1, 1)
        self.FireballGrid = QtWidgets.QGridLayout()
        self.FireballGrid.setObjectName("FireballGrid")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.FireballGrid.addItem(spacerItem, 5, 0, 1, 1)
        self.FireballImgLbl = QtWidgets.QLabel(self.PlayersFrame)
        self.FireballImgLbl.setText("")
        self.FireballImgLbl.setPixmap(QtGui.QPixmap("IMAGES/fire ball1.png"))
        self.FireballImgLbl.setScaledContents(True)
        self.FireballImgLbl.setObjectName("FireballImgLbl")
        self.FireballGrid.addWidget(self.FireballImgLbl, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.FireballGrid.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.FireballGrid.addItem(spacerItem2, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.FireballGrid.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.FireballGrid.addItem(spacerItem4, 1, 0, 1, 1)
        self.PlayerFrameGrid.addLayout(self.FireballGrid, 0, 1, 1, 1)
        self.TeamPlayersGrid = QtWidgets.QGridLayout()
        self.TeamPlayersGrid.setObjectName("TeamPlayersGrid")
        self.PointsUsedGrid = QtWidgets.QGridLayout()
        self.PointsUsedGrid.setObjectName("PointsUsedGrid")
        self.PointsUsedLbl = QtWidgets.QLabel(self.PlayersFrame)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.PointsUsedLbl.setFont(font)
        self.PointsUsedLbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.PointsUsedLbl.setObjectName("PointsUsedLbl")
        self.PointsUsedGrid.addWidget(self.PointsUsedLbl, 0, 0, 1, 1)
        self.PointsUsedValueLbl = QtWidgets.QLabel(self.PlayersFrame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PointsUsedValueLbl.setFont(font)
        self.PointsUsedValueLbl.setObjectName("PointsUsedValueLbl")
        self.PointsUsedGrid.addWidget(self.PointsUsedValueLbl, 0, 1, 1, 1)
        self.TeamPlayersGrid.addLayout(self.PointsUsedGrid, 0, 0, 1, 1)
        self.SelectedPlayersFrame = QtWidgets.QFrame(self.PlayersFrame)
        self.SelectedPlayersFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.SelectedPlayersFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SelectedPlayersFrame.setObjectName("SelectedPlayersFrame")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.SelectedPlayersFrame)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.SelectedPlayersGrid = QtWidgets.QGridLayout()
        self.SelectedPlayersGrid.setObjectName("SelectedPlayersGrid")
        self.TeamPlayersList = QtWidgets.QListWidget(self.SelectedPlayersFrame)
        self.TeamPlayersList.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.TeamPlayersList.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TeamPlayersList.setFont(font)
        self.TeamPlayersList.setStyleSheet("background-color: rgb(255, 255, 0,200);")
        self.TeamPlayersList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.TeamPlayersList.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.TeamPlayersList.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.TeamPlayersList.setProperty("isWrapping", False)
        self.TeamPlayersList.setResizeMode(QtWidgets.QListView.Adjust)
        self.TeamPlayersList.setWordWrap(True)
        self.TeamPlayersList.setObjectName("TeamPlayersList")
        self.SelectedPlayersGrid.addWidget(self.TeamPlayersList, 1, 0, 1, 1)
        self.YourTeamGrid = QtWidgets.QGridLayout()
        self.YourTeamGrid.setObjectName("YourTeamGrid")
        self.TeamNameLbl = QtWidgets.QLabel(self.SelectedPlayersFrame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TeamNameLbl.setFont(font)
        self.TeamNameLbl.setObjectName("TeamNameLbl")
        self.YourTeamGrid.addWidget(self.TeamNameLbl, 1, 0, 1, 1)
        self.TeamNameDisplayLbl = QtWidgets.QLabel(self.SelectedPlayersFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TeamNameDisplayLbl.sizePolicy().hasHeightForWidth())
        self.TeamNameDisplayLbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TeamNameDisplayLbl.setFont(font)
        self.TeamNameDisplayLbl.setText("")
        self.TeamNameDisplayLbl.setObjectName("TeamNameDisplayLbl")
        self.YourTeamGrid.addWidget(self.TeamNameDisplayLbl, 1, 1, 1, 1)
        self.SelectedPlayersGrid.addLayout(self.YourTeamGrid, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.SelectedPlayersGrid, 0, 0, 1, 1)
        self.TeamPlayersGrid.addWidget(self.SelectedPlayersFrame, 1, 0, 1, 1)
        self.PlayerFrameGrid.addLayout(self.TeamPlayersGrid, 0, 2, 1, 1)
        self.gridLayout_9.addLayout(self.PlayerFrameGrid, 1, 0, 1, 1)
        self.SelectGrpBox = QtWidgets.QGroupBox(self.PlayersFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectGrpBox.sizePolicy().hasHeightForWidth())
        self.SelectGrpBox.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 112, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 168, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 140, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 56, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 74, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 112, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 56, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 112, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 168, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 140, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 56, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 74, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 112, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 56, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 56, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 112, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 168, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 140, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 56, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 74, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 56, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 56, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 112, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 112, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 112, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.SelectGrpBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.SelectGrpBox.setFont(font)
        self.SelectGrpBox.setFlat(False)
        self.SelectGrpBox.setCheckable(False)
        self.SelectGrpBox.setObjectName("SelectGrpBox")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.SelectGrpBox)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.ArImgLbl = QtWidgets.QLabel(self.SelectGrpBox)
        self.ArImgLbl.setText("")
        self.ArImgLbl.setPixmap(QtGui.QPixmap("IMAGES/allrounder1.png"))
        self.ArImgLbl.setScaledContents(True)
        self.ArImgLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ArImgLbl.setObjectName("ArImgLbl")
        self.gridLayout_20.addWidget(self.ArImgLbl, 0, 4, 1, 1)
        self.BowGrid = QtWidgets.QGridLayout()
        self.BowGrid.setObjectName("BowGrid")
        self.BowLbl = QtWidgets.QLabel(self.SelectGrpBox)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.BowLbl.setFont(font)
        self.BowLbl.setObjectName("BowLbl")
        self.BowGrid.addWidget(self.BowLbl, 0, 0, 1, 1)
        self.BowNoLbl = QtWidgets.QLabel(self.SelectGrpBox)
        self.BowNoLbl.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.BowNoLbl.setFont(font)
        self.BowNoLbl.setObjectName("BowNoLbl")
        self.BowGrid.addWidget(self.BowNoLbl, 0, 1, 1, 1)
        self.gridLayout_20.addLayout(self.BowGrid, 0, 3, 1, 1)
        self.ArGrid = QtWidgets.QGridLayout()
        self.ArGrid.setObjectName("ArGrid")
        self.ArLbl = QtWidgets.QLabel(self.SelectGrpBox)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ArLbl.setFont(font)
        self.ArLbl.setObjectName("ArLbl")
        self.ArGrid.addWidget(self.ArLbl, 0, 0, 1, 1)
        self.ArNoLbl = QtWidgets.QLabel(self.SelectGrpBox)
        self.ArNoLbl.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ArNoLbl.setFont(font)
        self.ArNoLbl.setObjectName("ArNoLbl")
        self.ArGrid.addWidget(self.ArNoLbl, 0, 1, 1, 1)
        self.gridLayout_20.addLayout(self.ArGrid, 0, 5, 1, 1)
        self.WktImgLbl = QtWidgets.QLabel(self.SelectGrpBox)
        self.WktImgLbl.setText("")
        self.WktImgLbl.setPixmap(QtGui.QPixmap("IMAGES/wktkpr1.png"))
        self.WktImgLbl.setScaledContents(True)
        self.WktImgLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.WktImgLbl.setObjectName("WktImgLbl")
        self.gridLayout_20.addWidget(self.WktImgLbl, 0, 6, 1, 1)
        self.BatImgLbl = QtWidgets.QLabel(self.SelectGrpBox)
        self.BatImgLbl.setText("")
        self.BatImgLbl.setPixmap(QtGui.QPixmap("IMAGES/batsman1.png"))
        self.BatImgLbl.setScaledContents(True)
        self.BatImgLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BatImgLbl.setObjectName("BatImgLbl")
        self.gridLayout_20.addWidget(self.BatImgLbl, 0, 0, 1, 1)
        self.BatGrid = QtWidgets.QGridLayout()
        self.BatGrid.setObjectName("BatGrid")
        self.BatLbl = QtWidgets.QLabel(self.SelectGrpBox)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.BatLbl.setFont(font)
        self.BatLbl.setObjectName("BatLbl")
        self.BatGrid.addWidget(self.BatLbl, 0, 0, 1, 1)
        self.BatNoLbl = QtWidgets.QLabel(self.SelectGrpBox)
        self.BatNoLbl.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.BatNoLbl.setFont(font)
        self.BatNoLbl.setObjectName("BatNoLbl")
        self.BatGrid.addWidget(self.BatNoLbl, 0, 1, 1, 1)
        self.gridLayout_20.addLayout(self.BatGrid, 0, 1, 1, 1)
        self.WktGrid = QtWidgets.QGridLayout()
        self.WktGrid.setObjectName("WktGrid")
        self.WktLbl = QtWidgets.QLabel(self.SelectGrpBox)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.WktLbl.setFont(font)
        self.WktLbl.setObjectName("WktLbl")
        self.WktGrid.addWidget(self.WktLbl, 0, 0, 1, 1)
        self.WkNoLbl = QtWidgets.QLabel(self.SelectGrpBox)
        self.WkNoLbl.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.WkNoLbl.setFont(font)
        self.WkNoLbl.setObjectName("WkNoLbl")
        self.WktGrid.addWidget(self.WkNoLbl, 0, 1, 1, 1)
        self.gridLayout_20.addLayout(self.WktGrid, 0, 7, 1, 1)
        self.BowImgLbl = QtWidgets.QLabel(self.SelectGrpBox)
        self.BowImgLbl.setText("")
        self.BowImgLbl.setPixmap(QtGui.QPixmap("IMAGES/bowler1.png"))
        self.BowImgLbl.setScaledContents(True)
        self.BowImgLbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.BowImgLbl.setObjectName("BowImgLbl")
        self.gridLayout_20.addWidget(self.BowImgLbl, 0, 2, 1, 1)
        self.gridLayout_9.addWidget(self.SelectGrpBox, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.PlayersFrame, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1373, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 79, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 24, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 79, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 79, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(59, 0, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 79, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 24, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 79, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 79, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(59, 0, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 79, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 79, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 79, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.menubar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("background-color: rgb(255, 79, 0);")
        self.menubar.setObjectName("menubar")
        self.menu_Manage_Teams = QtWidgets.QMenu(self.menubar)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 167, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 46, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 38, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 15, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 20, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 167, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 167, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 15, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 167, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 46, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 38, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 15, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 20, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 167, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 167, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 15, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 15, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 167, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 46, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 38, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 15, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 20, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 15, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 15, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 167, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 167, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 31, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.menu_Manage_Teams.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menu_Manage_Teams.setFont(font)
        self.menu_Manage_Teams.setAcceptDrops(True)
        self.menu_Manage_Teams.setToolTipDuration(20)
        self.menu_Manage_Teams.setStyleSheet("background-color: rgb(247, 167, 29);")
        self.menu_Manage_Teams.setTearOffEnabled(False)
        self.menu_Manage_Teams.setToolTipsVisible(True)
        self.menu_Manage_Teams.setObjectName("menu_Manage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 20, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 30, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 25, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 10, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 13, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 20, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 10, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 20, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 30, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 25, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 10, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 13, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 20, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 10, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 10, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 20, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 30, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 25, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 10, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 13, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 10, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 10, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 20, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 20, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 20, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.statusbar.setPalette(palette)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("IMAGES/New.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNEW_Team.setIcon(icon1)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("IMAGES/Open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOPEN_Team.setIcon(icon2)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("IMAGES/Save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSAVE_Team.setIcon(icon3)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("IMAGES/evaluate1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEVALUATE_Team.setIcon(icon4)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menu_Manage_Teams.addAction(self.actionNEW_Team)
        self.menu_Manage_Teams.addAction(self.actionOPEN_Team)
        self.menu_Manage_Teams.addAction(self.actionSAVE_Team)
        self.menu_Manage_Teams.addSeparator()
        self.menu_Manage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menu_Manage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        self.PointsAvailLbl.setText(_translate("MainWindow", "Points Available"))
        self.PointsAvailValueLbl.setText(_translate("MainWindow", "0"))
        self.BatRadio.setText(_translate("MainWindow", "BAT"))
        self.BwlRadio.setText(_translate("MainWindow", "BOW"))
        self.ArRadio.setText(_translate("MainWindow", "AR"))
        self.WkRadio.setText(_translate("MainWindow", "WK"))
        self.PointsUsedLbl.setText(_translate("MainWindow", "Points Used"))
        self.PointsUsedValueLbl.setText(_translate("MainWindow", "0"))
        self.TeamNameLbl.setText(_translate("MainWindow", "Team Name : "))
        self.SelectGrpBox.setTitle(_translate("MainWindow", "Your Selections"))
        self.BowLbl.setText(_translate("MainWindow", "Bowler (BOW)"))
        self.BowNoLbl.setText(_translate("MainWindow", "0"))
        self.ArLbl.setText(_translate("MainWindow", "All Rounder (AR)"))
        self.ArNoLbl.setText(_translate("MainWindow", "0"))
        self.BatLbl.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.BatNoLbl.setText(_translate("MainWindow", "0"))
        self.WktLbl.setText(_translate("MainWindow", "Wicket - Keeper (WK)"))
        self.WkNoLbl.setText(_translate("MainWindow", "0"))
        self.menu_Manage_Teams.setTitle(_translate("MainWindow", " Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionNEW_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionOPEN_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionSAVE_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionEVALUATE_Team.setShortcut(_translate("MainWindow", "Ctrl+E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetNameDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GetNameDialog(object):
    def setupUi(self, GetNameDialog):
        GetNameDialog.setObjectName("GetNameDialog")
        GetNameDialog.resize(565, 171)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GetNameDialog.sizePolicy().hasHeightForWidth())
        GetNameDialog.setSizePolicy(sizePolicy)
        GetNameDialog.setMinimumSize(QtCore.QSize(565, 171))
        GetNameDialog.setMaximumSize(QtCore.QSize(565, 171))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IMAGES/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GetNameDialog.setWindowIcon(icon)
        GetNameDialog.setModal(True)
        self.GetTeamNameButtons = QtWidgets.QDialogButtonBox(GetNameDialog)
        self.GetTeamNameButtons.setGeometry(QtCore.QRect(460, 50, 81, 61))
        self.GetTeamNameButtons.setOrientation(QtCore.Qt.Vertical)
        self.GetTeamNameButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.GetTeamNameButtons.setCenterButtons(True)
        self.GetTeamNameButtons.setObjectName("GetTeamNameButtons")
        self.BackgroundLbl = QtWidgets.QLabel(GetNameDialog)
        self.BackgroundLbl.setGeometry(QtCore.QRect(0, -20, 571, 251))
        self.BackgroundLbl.setText("")
        self.BackgroundLbl.setPixmap(QtGui.QPixmap("IMAGES/ground2.jpg"))
        self.BackgroundLbl.setScaledContents(True)
        self.BackgroundLbl.setObjectName("BackgroundLbl")
        self.TeamNameLine = QtWidgets.QLineEdit(GetNameDialog)
        self.TeamNameLine.setGeometry(QtCore.QRect(110, 70, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TeamNameLine.setFont(font)
        self.TeamNameLine.setObjectName("TeamNameLine")
        self.CricketerImageLbl = QtWidgets.QLabel(GetNameDialog)
        self.CricketerImageLbl.setGeometry(QtCore.QRect(0, 0, 111, 171))
        self.CricketerImageLbl.setText("")
        self.CricketerImageLbl.setPixmap(QtGui.QPixmap("IMAGES/logo.png"))
        self.CricketerImageLbl.setScaledContents(True)
        self.CricketerImageLbl.setObjectName("CricketerImageLbl")
        self.EnterTeamNameLbl = QtWidgets.QLabel(GetNameDialog)
        self.EnterTeamNameLbl.setGeometry(QtCore.QRect(110, 40, 321, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(253, 253, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 253, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.EnterTeamNameLbl.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(12)
        self.EnterTeamNameLbl.setFont(font)
        self.EnterTeamNameLbl.setWordWrap(True)
        self.EnterTeamNameLbl.setObjectName("EnterTeamNameLbl")
        self.BackgroundLbl.raise_()
        self.GetTeamNameButtons.raise_()
        self.TeamNameLine.raise_()
        self.CricketerImageLbl.raise_()
        self.EnterTeamNameLbl.raise_()

        self.retranslateUi(GetNameDialog)
        self.GetTeamNameButtons.accepted.connect(GetNameDialog.accept)
        self.GetTeamNameButtons.rejected.connect(GetNameDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GetNameDialog)

    def retranslateUi(self, GetNameDialog):
        _translate = QtCore.QCoreApplication.translate
        GetNameDialog.setWindowTitle(_translate("GetNameDialog", "Fantasy Cricket"))
        self.TeamNameLine.setPlaceholderText(_translate("GetNameDialog", "Ex. My Team"))
        self.EnterTeamNameLbl.setText(_translate("GetNameDialog", "Enter Your Team Name Here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GetNameDialog = QtWidgets.QDialog()
    ui = Ui_GetNameDialog()
    ui.setupUi(GetNameDialog)
    GetNameDialog.show()
    sys.exit(app.exec_())
    <?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>GetNameDialog</class>
 <widget class="QDialog" name="GetNameDialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>565</width>
    <height>171</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="minimumSize">
   <size>
    <width>565</width>
    <height>171</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>565</width>
    <height>171</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Fantasy Cricket</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>IMAGES/logo.png</normaloff>IMAGES/logo.png</iconset>
  </property>
  <property name="modal">
   <bool>true</bool>
  </property>
  <widget class="QDialogButtonBox" name="GetTeamNameButtons">
   <property name="geometry">
    <rect>
     <x>460</x>
     <y>50</y>
     <width>81</width>
     <height>61</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Vertical</enum>
   </property>
   <property name="standardButtons">
    <set>QDialogButtonBox::Cancel|QDialogButtonBox::Ok</set>
   </property>
   <property name="centerButtons">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QLabel" name="BackgroundLbl">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>-20</y>
     <width>571</width>
     <height>251</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="pixmap">
    <pixmap>IMAGES/ground2.jpg</pixmap>
   </property>
   <property name="scaledContents">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QLineEdit" name="TeamNameLine">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>70</y>
     <width>321</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Comic Sans MS</family>
     <pointsize>12</pointsize>
     <weight>75</weight>
     <bold>true</bold>
    </font>
   </property>
   <property name="placeholderText">
    <string>Ex. My Team</string>
   </property>
  </widget>
  <widget class="QLabel" name="CricketerImageLbl">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>111</width>
     <height>171</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="pixmap">
    <pixmap>IMAGES/logo.png</pixmap>
   </property>
   <property name="scaledContents">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QLabel" name="EnterTeamNameLbl">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>40</y>
     <width>321</width>
     <height>21</height>
    </rect>
   </property>
   <property name="palette">
    <palette>
     <active>
      <colorrole role="WindowText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>253</red>
         <green>253</green>
         <blue>253</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Text">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>254</red>
         <green>254</green>
         <blue>254</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="PlaceholderText">
       <brush brushstyle="SolidPattern">
        <color alpha="128">
         <red>254</red>
         <green>254</green>
         <blue>254</blue>
        </color>
       </brush>
      </colorrole>
     </active>
     <inactive>
      <colorrole role="WindowText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>253</red>
         <green>253</green>
         <blue>253</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Text">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>254</red>
         <green>254</green>
         <blue>254</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="PlaceholderText">
       <brush brushstyle="SolidPattern">
        <color alpha="128">
         <red>254</red>
         <green>254</green>
         <blue>254</blue>
        </color>
       </brush>
      </colorrole>
     </inactive>
     <disabled>
      <colorrole role="WindowText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>120</red>
         <green>120</green>
         <blue>120</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Text">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>120</red>
         <green>120</green>
         <blue>120</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="PlaceholderText">
       <brush brushstyle="SolidPattern">
        <color alpha="128">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
     </disabled>
    </palette>
   </property>
   <property name="font">
    <font>
     <family>Ravie</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Enter Your Team Name Here</string>
   </property>
   <property name="wordWrap">
    <bool>true</bool>
   </property>
  </widget>
  <zorder>BackgroundLbl</zorder>
  <zorder>GetTeamNameButtons</zorder>
  <zorder>TeamNameLine</zorder>
  <zorder>CricketerImageLbl</zorder>
  <zorder>EnterTeamNameLbl</zorder>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>GetTeamNameButtons</sender>
   <signal>accepted()</signal>
   <receiver>GetNameDialog</receiver>
   <slot>accept()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>460</x>
     <y>120</y>
    </hint>
    <hint type="destinationlabel">
     <x>157</x>
     <y>139</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>GetTeamNameButtons</sender>
   <signal>rejected()</signal>
   <receiver>GetNameDialog</receiver>
   <slot>reject()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>486</x>
     <y>120</y>
    </hint>
    <hint type="destinationlabel">
     <x>286</x>
     <y>139</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>

    <?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MsgDialog</class>
 <widget class="QDialog" name="MsgDialog">
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>656</width>
    <height>414</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="minimumSize">
   <size>
    <width>656</width>
    <height>414</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>656</width>
    <height>414</height>
   </size>
  </property>
  <property name="palette">
   <palette>
    <active>
     <colorrole role="WindowText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Button">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>113</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Light">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>170</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Midlight">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>141</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Dark">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>56</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Mid">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>75</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Text">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="BrightText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ButtonText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Base">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Window">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>70</green>
        <blue>124</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Shadow">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="AlternateBase">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>56</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ToolTipBase">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>220</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ToolTipText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="PlaceholderText">
      <brush brushstyle="SolidPattern">
       <color alpha="128">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
    </active>
    <inactive>
     <colorrole role="WindowText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Button">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>113</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Light">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>170</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Midlight">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>141</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Dark">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>56</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Mid">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>75</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Text">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="BrightText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ButtonText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Base">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Window">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>70</green>
        <blue>124</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Shadow">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="AlternateBase">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>56</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ToolTipBase">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>220</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ToolTipText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="PlaceholderText">
      <brush brushstyle="SolidPattern">
       <color alpha="128">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
    </inactive>
    <disabled>
     <colorrole role="WindowText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>56</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Button">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>113</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Light">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>170</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Midlight">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>141</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Dark">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>56</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Mid">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>75</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Text">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>56</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="BrightText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ButtonText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>56</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Base">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>70</green>
        <blue>124</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Window">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>70</green>
        <blue>124</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Shadow">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="AlternateBase">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>113</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ToolTipBase">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>220</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ToolTipText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="PlaceholderText">
      <brush brushstyle="SolidPattern">
       <color alpha="128">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
    </disabled>
   </palette>
  </property>
  <property name="windowTitle">
   <string>Fantasy Cricket</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>IMAGES/logo.png</normaloff>IMAGES/logo.png</iconset>
  </property>
  <property name="modal">
   <bool>true</bool>
  </property>
  <widget class="QLabel" name="BackgroundImgLbl">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>661</width>
     <height>421</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="pixmap">
    <pixmap>IMAGES/ground2.jpg</pixmap>
   </property>
   <property name="scaledContents">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QWidget" name="layoutWidget">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>641</width>
     <height>381</height>
    </rect>
   </property>
   <layout class="QGridLayout" name="MsgGrid">
    <item row="0" column="0">
     <widget class="QLabel" name="ImageLbl">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="text">
       <string/>
      </property>
      <property name="pixmap">
       <pixmap>IMAGES/stumpedout.png</pixmap>
      </property>
      <property name="scaledContents">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item row="0" column="1">
     <widget class="QLabel" name="MessageLbl">
      <property name="enabled">
       <bool>true</bool>
      </property>
      <property name="font">
       <font>
        <family>Kristen ITC</family>
        <pointsize>14</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>Message</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignCenter</set>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item row="1" column="1">
     <widget class="QDialogButtonBox" name="OkButtonBox">
      <property name="palette">
       <palette>
        <active>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>70</green>
            <blue>124</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>105</green>
            <blue>186</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>87</green>
            <blue>155</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>35</green>
            <blue>62</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>46</green>
            <blue>82</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>156</red>
            <green>23</green>
            <blue>21</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>70</green>
            <blue>124</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>35</green>
            <blue>62</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="PlaceholderText">
          <brush brushstyle="SolidPattern">
           <color alpha="128">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
        </active>
        <inactive>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>70</green>
            <blue>124</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>105</green>
            <blue>186</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>87</green>
            <blue>155</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>35</green>
            <blue>62</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>46</green>
            <blue>82</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>156</red>
            <green>23</green>
            <blue>21</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>70</green>
            <blue>124</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>35</green>
            <blue>62</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="PlaceholderText">
          <brush brushstyle="SolidPattern">
           <color alpha="128">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
        </inactive>
        <disabled>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>35</green>
            <blue>62</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>70</green>
            <blue>124</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>105</green>
            <blue>186</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>87</green>
            <blue>155</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>35</green>
            <blue>62</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>46</green>
            <blue>82</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>35</green>
            <blue>62</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>35</green>
            <blue>62</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>70</green>
            <blue>124</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>70</green>
            <blue>124</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>70</green>
            <blue>124</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="PlaceholderText">
          <brush brushstyle="SolidPattern">
           <color alpha="128">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
        </disabled>
       </palette>
      </property>
      <property name="font">
       <font>
        <family>Ravie</family>
        <pointsize>12</pointsize>
       </font>
      </property>
      <property name="autoFillBackground">
       <bool>false</bool>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
      <property name="standardButtons">
       <set>QDialogButtonBox::Ok</set>
      </property>
      <property name="centerButtons">
       <bool>true</bool>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>OkButtonBox</sender>
   <signal>accepted()</signal>
   <receiver>MsgDialog</receiver>
   <slot>accept()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>248</x>
     <y>254</y>
    </hint>
    <hint type="destinationlabel">
     <x>157</x>
     <y>274</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>OkButtonBox</sender>
   <signal>rejected()</signal>
   <receiver>MsgDialog</receiver>
   <slot>reject()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>316</x>
     <y>260</y>
    </hint>
    <hint type="destinationlabel">
     <x>286</x>
     <y>274</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MessageDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MsgDialog(object):
    def setupUi(self, MsgDialog):
        MsgDialog.setObjectName("MsgDialog")
        MsgDialog.setEnabled(True)
        MsgDialog.resize(656, 414)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MsgDialog.sizePolicy().hasHeightForWidth())
        MsgDialog.setSizePolicy(sizePolicy)
        MsgDialog.setMinimumSize(QtCore.QSize(656, 414))
        MsgDialog.setMaximumSize(QtCore.QSize(656, 414))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 141, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 56, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 75, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 56, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 141, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 56, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 75, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 56, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 56, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 141, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 56, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 75, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 56, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 56, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MsgDialog.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IMAGES/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MsgDialog.setWindowIcon(icon)
        MsgDialog.setModal(True)
        self.BackgroundImgLbl = QtWidgets.QLabel(MsgDialog)
        self.BackgroundImgLbl.setGeometry(QtCore.QRect(0, 0, 661, 421))
        self.BackgroundImgLbl.setText("")
        self.BackgroundImgLbl.setPixmap(QtGui.QPixmap("IMAGES/ground2.jpg"))
        self.BackgroundImgLbl.setScaledContents(True)
        self.BackgroundImgLbl.setObjectName("BackgroundImgLbl")
        self.layoutWidget = QtWidgets.QWidget(MsgDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 641, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.MsgGrid = QtWidgets.QGridLayout(self.layoutWidget)
        self.MsgGrid.setContentsMargins(0, 0, 0, 0)
        self.MsgGrid.setObjectName("MsgGrid")
        self.ImageLbl = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageLbl.sizePolicy().hasHeightForWidth())
        self.ImageLbl.setSizePolicy(sizePolicy)
        self.ImageLbl.setText("")
        self.ImageLbl.setPixmap(QtGui.QPixmap("IMAGES/stumpedout.png"))
        self.ImageLbl.setScaledContents(True)
        self.ImageLbl.setObjectName("ImageLbl")
        self.MsgGrid.addWidget(self.ImageLbl, 0, 0, 1, 1)
        self.MessageLbl = QtWidgets.QLabel(self.layoutWidget)
        self.MessageLbl.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.MessageLbl.setFont(font)
        self.MessageLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.MessageLbl.setWordWrap(True)
        self.MessageLbl.setObjectName("MessageLbl")
        self.MsgGrid.addWidget(self.MessageLbl, 0, 1, 1, 1)
        self.OkButtonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 87, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 35, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 46, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(156, 23, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 35, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 87, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 35, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 46, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(156, 23, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 35, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 35, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 87, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 35, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 46, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 35, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 35, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.OkButtonBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(12)
        self.OkButtonBox.setFont(font)
        self.OkButtonBox.setAutoFillBackground(False)
        self.OkButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.OkButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.OkButtonBox.setCenterButtons(True)
        self.OkButtonBox.setObjectName("OkButtonBox")
        self.MsgGrid.addWidget(self.OkButtonBox, 1, 1, 1, 1)

        self.retranslateUi(MsgDialog)
        self.OkButtonBox.accepted.connect(MsgDialog.accept)
        self.OkButtonBox.rejected.connect(MsgDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MsgDialog)

    def retranslateUi(self, MsgDialog):
        _translate = QtCore.QCoreApplication.translate
        MsgDialog.setWindowTitle(_translate("MsgDialog", "Fantasy Cricket"))
        self.MessageLbl.setText(_translate("MsgDialog", "Message"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MsgDialog = QtWidgets.QDialog()
    ui = Ui_MsgDialog()
    ui.setupUi(MsgDialog)
    MsgDialog.show()
    sys.exit(app.exec_())
    import sqlite3
game_db = sqlite3.connect('cricket.db')
game_cursor = game_db.cursor()

def getPoints(team):
    points = 0
    for g in team:
        for p in g:
            points += getVal(p[0])
    return points

def getVal(player):
    query = 'SELECT Value FROM Stats WHERE Player = ?'
    game_cursor.execute(query, (player,))
    val =  game_cursor.fetchone()
    return val[0]

def getTeamScore(match, team):
    q = 'SELECT Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO FROM Match, Teams, '
    query = [ q + ' Batsmen WHERE Match.Player = Batsmen.Batsman AND Teams.Name = Batsmen.Name AND Match.MatchID = ? AND Teams.Name = ?',
             q + ' Bowlers WHERE Match.Player = Bowlers.Bowler AND Teams.Name = Bowlers.Name AND Match.MatchID = ? AND Teams.Name = ?',
             q + ' AllRounders WHERE Match.Player = AllRounders.AR AND Teams.Name = AllRounders.Name AND Match.MatchID = ? AND Teams.Name = ?',
             q + ' WicketKeeper WHERE Match.Player = WicketKeeper.WK AND Teams.Name = WicketKeeper.Name AND Match.MatchID = ? AND Teams.Name = ?']
    players = []
    for q in query:
        game_cursor.execute(q, (match, team))
        result = game_cursor.fetchall()
        for r in result:
            players.append(r)
    team_score = 0
    player_score = []
    for p in players:
        s = getPlayerScore(p)
        team_score += s
        player_score.append(s)
    player_score.insert(0,team_score)
    return player_score

def getPlayerScore(p):
    runs = p[0]
    faced = p[1]
    fours = p[2]
    sixes = p[3]
    bowled = p[4]
    maiden = p[5]
    given = p[6]
    wkts = p[7]
    catches = p[8]
    stumping = p[9]
    ro = p[10]
    score = runs/2 +fours + sixes * 2 + maiden * 4 + 10 * (wkts + catches + stumping + ro)
    if faced > 0:
        strike_rate = runs/faced * 100
    else:
        strike_rate = 0
    if bowled > 0:
        eco_rate = 6 * given/bowled
    else:
        eco_rate = 0
    if strike_rate > 100:
        score += 4
    elif strike_rate >= 80:
        score += 2
    if eco_rate < 2:
        score += 10
    elif eco_rate < 3.5:
        score += 7
    elif eco_rate < 4.5:
        score += 4
    if runs > 100:
        score += 10
    elif runs > 50:
        score += 5
    if wkts >= 5:
        score+=10
    elif wkts >= 3:
        score+=5

    return int(score)
    

