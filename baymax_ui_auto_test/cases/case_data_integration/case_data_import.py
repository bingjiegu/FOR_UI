from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys
from PageObject.data_integration_page.data_import_page.data_import_page import DataImportPage
from PageObject.home.home_page import HomePage
from PageObject.login.login_page import LoginTestPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)

class DataImportTest(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/数据导入.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()

    # 校验“数据导入-创建”任务
    def test_a043_create_data_import(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/data_import_yaml/数据导入-创建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DataImportPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-复制”任务
    def test_a044_copy_data_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/data_import_yaml/数据导入-复制.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DataImportPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-启用”任务
    def test_a053_start_data_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/data_import_yaml/数据导入-启用.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DataImportPage(app)
        page.operate()
        page.check_point()

class DataImportTest2(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/数据导入.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()

    # 校验“数据导入-执行列表”任务
    def test_a054_execute_list_data_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/data_import_yaml/数据导入-执行列表.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DataImportPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-预览数据集”任务
    def test_a055_preview_data_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/data_import_yaml/数据导入-预览数据集.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DataImportPage(app)
        page.operate()
        page.check_point()

    def setUp(self):
        super(DataImportTest2, self).setUpClass()
        self.to_resource_dir()

    def tearDown(self):
        super(DataImportTest2, self).tearDownClass()


    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()

