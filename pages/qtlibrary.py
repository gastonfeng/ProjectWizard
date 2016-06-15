# coding:utf-8

'''
作者：张潇健
日期：2016-6-14
概述：qt库选择
'''

from PyQt4.QtGui import QWizardPage,QHBoxLayout,QVBoxLayout,QLabel,QLineEdit,QPushButton,QCheckBox,QGridLayout
import app_datas

class QtLibraryPage(QWizardPage):

    def __init__(self):
        super(QtLibraryPage,self).__init__()
        self.setTitle('Qt模块')
        self.setSubTitle('设置Qt的模块引用')
        rootLayout = QVBoxLayout()
        rootLayout.setContentsMargins(20, 30, 20, 30)

        gLayout = QGridLayout()
        self.checkboxs = []
        index = 0
        for moudel in app_datas.g_qt_library:
            checkBox = QCheckBox(moudel['name'])
            if moudel['refer']:
                checkBox.setCheckState(2)
            row = index / 3
            offset = index % 3
            gLayout.addWidget(checkBox, row, offset)
            self.checkboxs.append(checkBox)
            index += 1

        rootLayout.addLayout(gLayout)
        self.setLayout(rootLayout)

    def validatePage(self):
        librarys = []
        for i in range(len(self.checkboxs)):
            if self.checkboxs[i].checkState() == 2:
                librarys.append(app_datas.g_qt_library[i])

        app_datas.g_configurations['qt_library'] = librarys
        return True