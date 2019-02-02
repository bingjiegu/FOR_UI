from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys
from PageObject.data_integration_page.resourceMan_page.resourceMan_page import ResourceManPage
from PageObject.home.home_page import HomePage
from PageObject.login.login_page import LoginTestPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), p)
)

class OperateDirTest(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/资源目录.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()

    # 校验“打开数据标准文件夹”
    def test_a017_open_dir(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/展开文件夹.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“闭合数据标准文件夹”
    def test_a018_close_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/闭合文件夹.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“新建数据标准文件夹”
    def test_a019_create_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/新建文件夹.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

     # 校验“删除数据标准文件夹”
    def test_a020_delete_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/删除文件夹.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“移动数据标准文件夹”
    def test_a021_move_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/移动文件夹.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“创建jdbc数据源”
    def test_a022_create_dbsource_jdbc(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-新建JDBC数据源.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()
    # 校验“创建jdbc数据源-链接测试”
    def test_a023_create_dbsource_jdbc_connect(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-新建JDBC数据源-链接测试.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()
    # 校验“删除jdbc数据源”
    def test_a024_delete_dbsource_jdbc(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-删除JDBC数据源.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“元数据-创建schema”
    def test_a025_create_schema(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/元数据-新建schema.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(OperateDirTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(OperateDirTest, cls).tearDownClass()

if __name__ == "__main__":
    unittest.main()

