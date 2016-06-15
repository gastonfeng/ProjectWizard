# coding:utf-8

'''
作者：张潇健
日期：2016-6-14
概述：工程信息
'''

from PyQt4.QtGui import QWizard,QWizardPage,QHBoxLayout,QVBoxLayout,QLabel,QLineEdit,QPushButton,QFileDialog,QComboBox
from PyQt4.QtCore import QString,QStringList,SIGNAL
import app_datas
import os
import json

class BaseInfoPage(QWizardPage):

    def __init__(self):
        super(BaseInfoPage,self).__init__()

        self.setTitle('工程信息')
        self.setSubTitle('设置工程的基本信息')
        rootLayout = QVBoxLayout()
        rootLayout.setContentsMargins(20, 30, 20, 30)

        self.project_name = ""
        self.project_dir = ""
        self.completed = False

        row1 = QHBoxLayout()
        lable1 = QLabel('工程名称：')
        self.et_project_name = QLineEdit()
        self.et_project_name.textChanged.connect(self.on_text_changed)
        row1.addWidget(lable1)
        row1.addWidget(self.et_project_name)
        row1.addSpacing(200)

        row2 = QHBoxLayout()
        lable2 = QLabel('工程位置：')
        self.et_project_location = QLineEdit()
        self.et_project_location.textChanged.connect(self.on_text_changed)
        self.et_project_location.setReadOnly(True)
        btn_location = QPushButton('...')
        btn_location.setFixedWidth(50)
        btn_location.clicked.connect(self.getSavePath)
        row2.addWidget(lable2)
        row2.addWidget(self.et_project_location)
        row2.addWidget(btn_location)

        row3 = QHBoxLayout()
        lable3 = QLabel('源模板  ：')
        self.cb_wizard_type = QComboBox()
        items = QStringList()
        for key in app_datas.g_templates:
            items.append(key)
        self.cb_wizard_type.addItems(items)
        row3.addWidget(lable3)
        row3.addWidget(self.cb_wizard_type)
        row3.addStretch(0)

        rootLayout.addLayout(row1)
        rootLayout.addLayout(row2)
        rootLayout.addLayout(row3)
        self.setLayout(rootLayout)

    def getSavePath(self):
        path = QFileDialog.getExistingDirectory()
        self.et_project_location.setText(path)

    def test_completed(self):
        project_name = self.et_project_name.text().trimmed()
        project_dir = self.et_project_location.text().trimmed()
        return not project_name.isEmpty() and not project_dir.isEmpty()

    def on_text_changed(self,text):
        self.isComplete()

    def isComplete(self):
        ret = self.test_completed()
        if ret != self.completed:
            self.completed = ret
            self.emit(SIGNAL("completeChanged()"))
        return ret

    def validatePage(self):
        project_name = self.et_project_name.text().trimmed()
        project_dir = self.et_project_location.text().trimmed()
        wizard_template = self.cb_wizard_type.currentText()
        app_datas.g_configurations['project_name'] = str(project_name.toUtf8())
        app_datas.g_configurations['project_uname'] = str(project_name.toUpper().toUtf8())
        app_datas.g_configurations['project_lname'] = str(project_name.toLower().toUtf8())
        app_datas.g_configurations['project_location'] = str(project_dir.toUtf8())
        app_datas.g_configurations['template_name'] = str(wizard_template.toUtf8())

        template_name = app_datas.g_configurations['template_name']
        template_dir = app_datas.g_pwd + os.sep + 'templates' + os.sep + template_name
        with open(template_dir + os.sep + 'config.json', 'r') as f:
            content = f.read()
        ret_json = app_datas.render(content, config=app_datas.g_configurations)
        app_datas.g_config = json.loads(ret_json)
        return True