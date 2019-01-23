# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from common.BaseRunner import ParametrizedTestCase
from cases.case_login import LoginTest33
from cases.case_login2 import LoginTest233
import unittest
from datetime import datetime
from common.TearDown import mk_file
from common.Count import countDate,writeExcel
from common.Email import send

def runnerCaseApp():
    start_time = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(LoginTest33))
    suite.addTest(ParametrizedTestCase.parametrize(LoginTest233))
    unittest.TextTestRunner(verbosity=2).run(suite)
    end_time = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((end_time - start_time).seconds) + "秒")

if __name__ == '__main__':
    mk_file()
    runnerCaseApp()
    writeExcel()
    send()

