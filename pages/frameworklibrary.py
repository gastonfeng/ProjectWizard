# coding:utf-8

'''
作者：张潇健
日期：2016-6-14
概述：框架模块选择
'''

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWizardPage

from ProjectWizard import app_datas


class FrameworkLibraryPage(QWizardPage):
    def __init__(self):
        super(FrameworkLibraryPage, self).__init__()
        self.completed = False
        self.setTitle('框架模块')
        self.setSubTitle('设置框架的模块引用')
        rootLayout = QVBoxLayout()
        rootLayout.setContentsMargins(20, 30, 20, 30)

        row2 = QHBoxLayout()
        lable2 = QLabel('框架根目录：')
        self.et_framework_root = QLineEdit()
        self.et_framework_root.setReadOnly(True)
        btn_location = QPushButton('...')
        btn_location.clicked.connect(self.on_select)
        btn_location.setFixedWidth(50)
        row2.addWidget(lable2)
        row2.addWidget(self.et_framework_root)
        row2.addWidget(btn_location)

        self.gLayout = QGridLayout()

        rootLayout.addLayout(row2)
        rootLayout.addLayout(self.gLayout)
        self.setLayout(rootLayout)

    def initializePage(self):
        super(FrameworkLibraryPage, self).initializePage()
        self.checkboxs = []
        index = 0
        for moudel in app_datas.g_config['moudels']:
            checkBox = QCheckBox(moudel['name'])
            if moudel['refer']:
                checkBox.setCheckState(2)
            row = index / 3
            offset = index % 3
            self.gLayout.addWidget(checkBox, row, offset)
            self.checkboxs.append(checkBox)
            index += 1

    def validatePage(self):
        librarys = []
        for i in range(len(self.checkboxs)):
            if self.checkboxs[i].checkState() == 2:
                librarys.append(app_datas.g_config['moudels'][i])

        app_datas.g_configurations['moudels'] = librarys
        framework_root = self.et_framework_root.text().trimmed()
        app_datas.g_configurations['framework_path'] = str(framework_root.toUtf8())
        return True

    def on_select(self):
        path = QFileDialog.getExistingDirectory()
        self.et_framework_root.setText(path)
        self.isComplete()

    def test_completed(self):
        framework_root = self.et_framework_root.text().trimmed()
        return not framework_root.isEmpty()

    def isComplete(self):
        ret = self.test_completed()
        if ret != self.completed:
            self.completed = ret
            self.emit(pyqtSignal("completeChanged()"))
        return ret
