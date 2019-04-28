# -*- coding: utf-8 -*-

from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys
from PageObject.data_integration_page.file_management_page.file_management_page import FileManagementPage
from PageObject.home.home_page import HomePage
from PageObject.login.login_page import LoginTestPage
from common.ElementParam import ElementParam

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)

class FileManagementTest(ParametrizedTestCase):
    fileManagement_url = ElementParam.HOST + "/#/dataMan" # 文件管理URL
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/文件管理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()

    #链接到某url装饰器
    def get_url(to_url):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                self.driver.get(to_url)
                func(self, *args, **kwargs)
            return wrapper
        return decorator

    # 校验“数据导入-进入文件夹”任务
    def test_a045_data_import_into_dir(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/file_management_yaml/文件管理-进入文件夹.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FileManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-返回上一级路径”任务
    def test_a046_data_import_cdup(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/file_management_yaml/文件管理-上一级.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FileManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-返回根目录”任务
    def test_a047_data_import_root_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/file_management_yaml/文件管理-返回根目录.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FileManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-创建目录”任务
    def test_a048_data_import_create_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/file_management_yaml/文件管理-创建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FileManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-删除目录”任务
    def test_a049_data_import_delete_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/file_management_yaml/文件管理-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FileManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-下载”任务
    def test_a050_data_import_download(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/file_management_yaml/文件管理-下载.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FileManagementPage(app)
        page.operate()
        page.check_point()

     # 校验“数据导入-上传”任务
    @get_url(fileManagement_url)
    def test_a051_data_import_upload(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/file_management_yaml/文件管理-上传.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FileManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-删除全部”任务
    @get_url(fileManagement_url)
    def test_a052_data_import_delete_all(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/file_management_yaml/文件管理-删除全部.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FileManagementPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(FileManagementTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(FileManagementTest, cls).tearDownClass()

if __name__ == "__main__":
    unittest.main()