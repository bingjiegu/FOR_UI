from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys
from PageObject.login.login_page import LoginTest

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class LoginTest33(ParametrizedTestCase):
    def testlogin(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/login/login.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTest(app)
        page.operate()
        page.check_point()


    @classmethod
    def setUpClass(cls):
        super(LoginTest33, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LoginTest33, cls).tearDownClass()

if __name__ == "__main__":
    unittest.main()








