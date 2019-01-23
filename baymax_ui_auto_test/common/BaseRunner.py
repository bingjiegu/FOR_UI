import unittest, os
from common.Logger import myLog
from selenium import webdriver
from common.ElementParam import ElementParam

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

def get_driver():
    chromedriver = PATH("../exe/chromedriver.exe")
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.maximize_window()  # 将浏览器最大化
    # driver = webdriver.Chrome()
    driver.get(ElementParam.URL)
    return driver

class ParametrizedTestCase(unittest.TestCase):

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)

    @classmethod
    def setUpClass(cls):
        pass
        cls.driver = get_driver()
        cls.logTest = myLog().getLog("chrome")  # 每个设备实例化一个日志记录器

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        pass

    def tearDown(self):
        pass

    @staticmethod
    def parametrize(testcase_klass, param=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite
