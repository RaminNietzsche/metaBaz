# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import GNrc

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(545, 329)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("image/10649.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 501, 291))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(_fromUtf8("     border-style: outset;\n"
"     border-width:2px;\n"
"     border-radius: 10px;\n"
"     border-color: black;\n"
"     font: bold 14px;\n"
"     margin-left:0;\n"
"     margin-right:0;\n"
"     position:absolute;\n"
"     opacity: 0.4; \n"
"     \n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));\n"
""))
        self.textEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "درباره‌ی نگار و من", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<meta content=\"1\" name=\"qrichtext\" />\n<style type=\"text/css\">p, li { white-space: pre-wrap; }\n</style>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/image/image/Raaaaaaaaam2.jpg\" style=\"float: left;\" width=\"100\" /></p>\n\n<p align=\"center\" dir=\"rtl\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">داستان از یک شبِ سردِ زمستانی شروع شد در محورِ کرمان-مشهد. داشتم رادیو گیگ گوش می کردم و سوتی جناب مک آفی و خلاصه از فرطِ بی&zwnj;کاری به این نتیجه رسیدم یک چیزی بنویسم که این متا-تگ ها را بردارو الته این لامصب ها روی همه جور فایلی می&zwnj;نشینند، ولی قدم اول عکس&zwnj;ها بود که پر استفاده تر و خطرناک&zwnj;ترند.</span></p>\n\n<p align=\"center\" dir=\"rtl\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">از قالبِ اصلی نگار برایِ این پروژه استفاده کردم چون حوصله نداشتم یکی جدید درست کنم. و همچنان هر گونه ارتباطی را با خودِ نگار تکذیب می&zwnj;کنم حالا اگر مریم باشد یا چیزی شبیه به آن باز یک چیزی ولی نگار نه!</span></p>\n\n<p align=\"center\" dir=\"rtl\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">متا-تگ باز، باز اش از باختن آمده، نه اوپن سورس و چیزهایی شبیه اه آن یعنی شما متا-تگ ها را از دست می&zwnj;دهید با آن.</span></p>\n\n<p align=\"center\" dir=\"rtl\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">اگر دوست داشتید اشکالات و نظراتِ&zwnj;تان را در موردِ </span><span style=\" font-size:11pt; font-weight:400; color:#ff007f;\">نگار</span><span style=\" font-size:11pt; font-weight:400;\"> (شخصِ خودش و یا پروژه&zwnj;اش با من در میان بگذارید)</span> و یا در مورد متا-باز</p>\n\n<p>&nbsp;</p>\n\n<p align=\"center\" dir=\"rtl\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" fo font-size:13pt; font-weight:400;\">آدرس ایمیل من : Ramin.Najarbashi@Gmail.com</span></p>\n\n<p align=\"center\" dir=\"rtl\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">همین!</span></p>\n\n<p align=\"center\" dir=\"rtl\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">آدرس پروژه در گیت هاب:</p>\n\n<p align=\"center\" dir=\"rtl\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/RaminNietzsche/Negar\">https://github.com/RaminNietzsche/metaBaz</a></p>\n\n<p align=\"center\" dir=\"rtl\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&nbsp;</p>\n", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

