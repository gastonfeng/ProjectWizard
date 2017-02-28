#coding:utf-8
import os
import sys

from PyQt5.QtCore import QTextCodec
from PyQt5.QtWidgets import QApplication

from ProjectWizard import app_datas
from ProjectWizard import wizard


def main():
    app = QApplication(sys.argv)
    tc = QTextCodec.codecForName('utf-8')
    # QTextCodec.setCodecForCStrings(tc)
    QTextCodec.setCodecForLocale(tc)
    # QTextCodec.setCodecForTr(tc)
    app_datas.g_pwd = os.getcwd()
    print(app_datas.g_pwd)

    #遍历目录
    tmpdirs = os.listdir(app_datas.g_pwd + os.sep + 'templates')
    for tmpdir in tmpdirs:
        currentdir = app_datas.g_pwd + os.sep + 'templates' + os.sep + tmpdir
        if os.path.isdir(currentdir) and os.path.exists(currentdir + os.sep + 'config.json'):
            app_datas.g_templates.append(tmpdir)

    dlg = wizard.MyWizard()
    dlg.show()
    app.exec_()

if __name__ == "__main__":
    main()



