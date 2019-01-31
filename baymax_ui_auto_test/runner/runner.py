# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from common.BaseRunner import ParametrizedTestCase
from cases.case_home.case_home_page_click import HomePageTest
from cases.case_login import LoginTest
from cases.case_data_integration.case_resourceMan.case_operate_dir import OperateDirTest
import unittest
from datetime import datetime
from common.TearDown import mk_file
from common.Count import countDate,writeExcel
from common.Email import send

def runnerCaseApp():
    start_time = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(LoginTest))
    suite.addTest(ParametrizedTestCase.parametrize(HomePageTest))
    suite.addTest(ParametrizedTestCase.parametrize(OperateDirTest))
    unittest.TextTestRunner(verbosity=2).run(suite)
    end_time = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((end_time - start_time).seconds) + "秒")

if __name__ == '__main__':
    mk_file()
    runnerCaseApp()
    writeExcel()
    send()
