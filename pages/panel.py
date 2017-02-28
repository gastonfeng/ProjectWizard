# coding:utf-8

'''
作者：张潇健
日期：2016-6-14
概述：列举之前向导的用户设定
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWizardPage

from ProjectWizard import app_datas
from ProjectWizard.pages.baseinfo import QStringList


class PanelPage(QWizardPage):

    def __init__(self):
        super(PanelPage,self).__init__()
        self.setTitle('最终生成')
        self.setSubTitle('显示工程配置的简要信息和即将生成的文件')

    def initializePage(self):
        super(PanelPage, self).initializePage()

        rootLayout = QVBoxLayout()
        rootLayout.setContentsMargins(20, 30, 20, 30)

        row0 = QHBoxLayout()
        lable0 = QLabel('引用模块：')
        lable0.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.lw_files = QListWidget()
        items0 = QStringList()
        for moudel in app_datas.g_configurations['moudels']:
            items0.append(moudel['name'])
        self.lw_files.addItems(items0)
        row0.addWidget(lable0)
        row0.addWidget(self.lw_files)

        row1 = QHBoxLayout()
        lable1 = QLabel('工程文件：')
        lable1.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.lw_files = QListWidget()
        items1 = QStringList()
        for file in app_datas.g_config['files']:
            items1.append(file['target'])
        self.lw_files.addItems(items1)
        row1.addWidget(lable1)
        row1.addWidget(self.lw_files)

        rootLayout.addLayout(row0)
        rootLayout.addLayout(row1)
        self.setLayout(rootLayout)

    def validatePage(self):
        pass
        return True