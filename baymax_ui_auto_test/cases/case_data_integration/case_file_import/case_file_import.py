# -*- coding: utf-8 -*-

from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys
from PageObject.data_integration_page.file_import_page.file_import_page import FileImportPage
from PageObject.home.home_page import HomePage
from PageObject.login.login_page import LoginTestPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), p)
)

class FileImportTest(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/文件导入.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()

    # 校验“创建文件导入任务”
    def test_a058_create_file_import(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/file_import_yaml/文件导入-创建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FileImportPage(app)
        page.operate()
        page.check_point()


    # 校验“复制文件导入任务”
    def test_a059_copy_file_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/file_import_yaml/文件导入-复制.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FileImportPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(FileImportTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(FileImportTest, cls).tearDownClass()