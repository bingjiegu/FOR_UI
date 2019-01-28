from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys
from PageObject.home.home_page import HomePage
from PageObject.login.login_page import LoginTestPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)
class HomePageTest(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/login/login.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    # 校验“资源目录”页面
    def test_a002_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/资源目录.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验“文件管理”页面
    def test_a003_file_manage(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/文件管理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入”
    def test_a004_data_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/数据导入.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验“文件导入”
    def test_a005_file_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/文件导入.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验“采集器”
    def test_a006_file_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/采集器.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据治理--质量分析”
    def test_a007_quality_analyze(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/质量分析.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

       # 校验 “数据治理--质量分析”
    def test_a008_blood_analyze(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/血缘分析.yaml"),
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


