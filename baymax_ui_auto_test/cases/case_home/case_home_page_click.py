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

    # 校验 “数据治理--血缘分析”
    def test_a008_blood_analyze(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/血缘分析.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据治理--血缘分析”
    def test_ba009_schema_analyze(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/元数据分析.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据治理--流程管理”
    def test_a009_flow_manage(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/流程管理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据治理--项目目录”
    def test_a010_project_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/项目目录.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据监控--运维管控”
    def test_a011_operations_control(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/运维管控.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据监控--访问监控yaml”
    def test_a012_inquiry_control(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/访问监控1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据监控--任务监控.yaml”
    def test_a013_task_control(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/任务监控.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “实时计算--作业管理.yaml”
    def test_a014_work_manage(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/作业管理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “实时计算--作业运维.yaml”
    def test_a015_work_operations(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/作业运维.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “实时计算--作业模板.yaml”
    def test_a016_work_template(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/作业模板.yaml"),
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


