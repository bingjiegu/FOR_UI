# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from common.BaseRunner import ParametrizedTestCase
from cases.case_home.case_home_page_click import HomePageTest
from cases.case_login import LoginTest
from cases.case_data_integration.case_resourceMan.case_operate_dir import OperateDirTest, OperateDirTest2
from cases.case_data_integration.case_data_import import DataImportTest, DataImportTest2
from cases.case_data_integration.case_file_management import FileManagementTest
from cases.case_data_integration.case_collector.case_collector import CollectorTemplateTest, CollectorimportDataTest, CollectorTaskListTest
from cases.case_data_integration.case_file_import.case_file_import import FileImportTest
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
    suite.addTest(ParametrizedTestCase.parametrize(OperateDirTest2))
    suite.addTest(ParametrizedTestCase.parametrize(DataImportTest))
    suite.addTest(ParametrizedTestCase.parametrize(DataImportTest2))
    suite.addTest(ParametrizedTestCase.parametrize(FileManagementTest))
    suite.addTest(ParametrizedTestCase.parametrize(FileImportTest))
    suite.addTest(ParametrizedTestCase.parametrize(CollectorTemplateTest))
    suite.addTest(ParametrizedTestCase.parametrize(CollectorimportDataTest))
    suite.addTest(ParametrizedTestCase.parametrize(CollectorTaskListTest))

    unittest.TextTestRunner(verbosity=2).run(suite)
    end_time = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((end_time - start_time).seconds) + "秒")

if __name__ == '__main__':
    mk_file()
    runnerCaseApp()
    writeExcel()
    send()
