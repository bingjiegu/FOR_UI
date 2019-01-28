from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys
from PageObject.home.home_page import HomePage
from PageObject.login.login_page import LoginTestPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)
class HomePageTest(ParametrizedTestCase):
    def login(self):
        print('bbbbbbbb:',PATH("../YAML/login/login.yaml"))
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/login/login.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    # 校验“资源目录”页面
    def test_a0_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/资源目录.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验“文件管理”页面
    def test_a1_file_manage(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/文件管理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验“文件导入”
    def test_a3_file_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/文件导入.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()


    @classmethod
    def setUpClass(cls):
        super(HomePageTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomePageTest, cls).tearDownClass()

if __name__ == "__main__":
    unittest.main()


