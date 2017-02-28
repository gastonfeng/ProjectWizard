# coding:utf-8

'''
作者：张潇健
日期：2016-6-13
概述：用来弹出向导
'''
import os

from PyQt5.QtWidgets import QWizard

from ProjectWizard import app_datas
from ProjectWizard.pages import baseinfo
from ProjectWizard.pages import frameworklibrary
from ProjectWizard.pages import panel
from ProjectWizard.pages import qtlibrary

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class MyWizard(QWizard):
    '''
    向导类
    '''
    def __init__(self):
        super(MyWizard,self).__init__()
        self.setWindowTitle('框架工程向导')
        self.setWizardStyle(QWizard.MacStyle)
        self.setOption(QWizard.IndependentPages,True)
        #self.setPixmap(QWizard.BackgroundPixmap,QPixmap('bj.jpg'))
        self.addPage(baseinfo.BaseInfoPage())
        self.addPage(qtlibrary.QtLibraryPage())
        self.addPage(frameworklibrary.FrameworkLibraryPage())
        self.addPage(panel.PanelPage())
        self.button(QWizard.NextButton).setEnabled(False)

    def accept(self):
        template_name = app_datas.g_configurations['template_name']
        template_dir = app_datas.g_pwd + os.sep + 'templates' + os.sep + template_name
        for file in app_datas.g_config['files']:
            sourcepath = template_dir + os.sep + file['source']
            targetpath = app_datas.g_configurations['project_location'] + os.sep + file['target']
            with open(sourcepath,'r') as f:
                content = f.read()
                content = app_datas.render(content,config = app_datas.g_configurations)
            with open(targetpath,'w+') as f:
                f.write(content.encode('utf-8'))
        super(MyWizard, self).accept()

    def validateCurrentPage(self):
        print(self.currentId())
        return super(MyWizard, self).validateCurrentPage()