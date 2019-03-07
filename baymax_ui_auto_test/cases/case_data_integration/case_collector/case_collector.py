from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys, time
from PageObject.data_integration_page.collector_page.collector_page import CollectorPage
from PageObject.home.home_page import HomePage
from PageObject.login.login_page import LoginTestPage
from common.ElementParam import ElementParam

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), p)
)

# 采集器列表页
class CollectorTemplateTest(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/采集器.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()

    # 校验“注册采集器”
    def test_a060_create_collector(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_template_yaml/采集器-注册.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“编辑采集器”
    def test_a061_edit_collector(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_template_yaml/采集器-编辑.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

     # 校验“删除采集器”
    def test_a062_delete_collector(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_template_yaml/采集器-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(CollectorTemplateTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(CollectorTemplateTest, cls).tearDownClass()


# 采集器 导入任务页测试
class CollectorimportDataTest(ParametrizedTestCase):
    importData_url = ElementParam.IMPORT_DATA_URL
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/采集器.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()

    #链接到某url装饰器
    def get_url(url):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                self.driver.get(url)
                func(self, *args, **kwargs)
            return wrapper
        return decorator

    # 校验“校验导入任务页”
    def test_a063_collector_import_data(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-列表.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

     # 校验“校验导入任务-同步任务信息”
    def test_a064_collector_import_data_sync(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-同步任务信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务页-数据源表预览”
    def test_a065_collector_import_data_source(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-数据源表预览.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务页-预览”
    def test_a066_collector_import_data_preview(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-预览.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()


    # 校验“校验导入任务页-预览-关闭”
    def test_a067_collector_import_data_close(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-预览-关闭.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务页-预览-确定”
    def test_a068_collector_import_data_ok(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-预览-确定.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务页-执行”
    def test_a069_collector_import_data(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-执行.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务-执行列表-查看日志”
    @get_url(importData_url)
    def test_a070_collector_import_data_view_log(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-执行列表-查看日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务-执行列表-查看错误日志”
    @get_url(importData_url)
    def test_a071_collector_import_data_view_error_log(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-执行列表-查看错误日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()


    @classmethod
    def setUpClass(cls):
        super(CollectorimportDataTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(CollectorimportDataTest, cls).tearDownClass()


# 采集器 任务页测试
class CollectorTaskListTest(ParametrizedTestCase):
    view_url = ElementParam.VIEW_URL  # 详细信息页
    taskList_url = ElementParam.TASK_LIST_URL  # 任务列表页
    dir_url = ElementParam.DIR_URL     # 资源目录页

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/采集器.yaml"),
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

    # 校验“校验导入任务-执行列表-查看日志”
    def test_a072_collector_dir(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-资源目录-页面校验.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务-执行列表-查看日志”
    @get_url(dir_url)
    def test_a073_collector_dir_sync(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-资源目录-同步.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(CollectorTaskListTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(CollectorTaskListTest, cls).tearDownClass()

