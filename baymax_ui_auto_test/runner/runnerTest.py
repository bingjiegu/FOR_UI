# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from common.BaseRunner import ParametrizedTestCase, get_driver
from cases.case_home.case_home_page_click import HomePageTest
from cases.case_home.case_home_page_for_dam import HomePageTest_Dam
from cases.case_home.case_home_page_for_Beiruan import HomePageTest_Beiruan
from cases.case_home.case_home_page_cab import HomePageTest_Cab
from cases.case_home.case_home_page_for_cad import HomePageTest_Cad
from cases.case_home.case_home_page_for_yinpao import HomePageTest_Yinpao
from cases.case_home.case_home_page_for_shubo import HomePageTest_Shubo


from cases.case_login import LoginTest
from cases.case_data_integration.case_resourceMan.case_operate_dir import OperateDirTest
from cases.case_data_integration.case_data_import import DataImportTest
from cases.case_data_integration.case_file_management import FileManagementTest
from cases.case_data_integration.case_collector.case_collector import CollectorTemplateTest, CollectorimportDataTest, CollectorTaskListTest
from cases.case_data_integration.case_file_import.case_file_import import FileImportTest
from cases.case_data_monitor.case_operational_monitoring.case_operational_monitoring import OperationalMonitoringTest
from cases.case_data_monitor.case_task_control.case_task_control import TaskControlTest
from cases.cases_data_govern.case_quality_analyze.case_quality_analyze import QualityAnalyzeTest
from cases.cases_data_govern.case_blood_analyze.case_blood_analyze import BloodAnalyzeTest
from cases.cases_data_govern.case_schema_analyze.case_schema_analyze import SchemaAnalyzeTest
from cases.case_data_analyze.case_flow_management.case_flow_management import FlowManagementTest
from cases.case_data_analyze.case_project_dir.case_project_dir import ProjectDirTest



from cases.case_home.case_home_page_click import HomePageTest_SSSS
from cases.case_home.case_home_page_for_dam import HomePageTest_Dam_SSSS
from cases.case_data_integration.case_resourceMan.case_operate_dir import OperateDirTestSSSS
from cases.case_data_integration.case_data_import import DataImportTest_SSSS
from cases.case_data_integration.case_file_management import FileManagementTest_SSSS
from cases.case_data_integration.case_collector.case_collector import CollectorTemplateTest_SSSS, CollectorimportDataTest_SSSS, CollectorTaskListTest_SSSS
from cases.case_data_monitor.case_operational_monitoring.case_operational_monitoring import OperationalMonitoringTest_SSSS
from cases.case_data_monitor.case_task_control.case_task_control import TaskControlTest_SSSS
from cases.cases_data_govern.case_quality_analyze.case_quality_analyze import QualityAnalyzeTest_SSSS
from cases.case_data_analyze.case_flow_management.case_flow_management import FlowManagementTest_SSSS
from cases.case_data_analyze.case_project_dir.case_project_dir import ProjectDirTest_SSSS
import unittest
from datetime import datetime
from common.TearDown import mk_file
from common.Count import countDate, writeExcel
from common.Email import send


def suite_case(who):
    suite = unittest.TestSuite()
    Check_module = {
        # 'Dam': [LoginTest, HomePageTest_Dam, OperateDirTest, DataImportTest, FileManagementTest, FileImportTest, CollectorTemplateTest,
        #            CollectorimportDataTest, CollectorTaskListTest, OperationalMonitoringTest, TaskControlTest, QualityAnalyzeTest,
        #            BloodAnalyzeTest, SchemaAnalyzeTest, FlowManagementTest, ProjectDirTest],
        # 'bayMax': [LoginTest, HomePageTest, OperateDirTest, DataImportTest, FileManagementTest, FileImportTest, CollectorTemplateTest,
        #            CollectorimportDataTest, CollectorTaskListTest, OperationalMonitoringTest, TaskControlTest, QualityAnalyzeTest,
        #            BloodAnalyzeTest, SchemaAnalyzeTest, FlowManagementTest, ProjectDirTest],
        # 'Beiruan': [LoginTest, HomePageTest_Beiruan, OperateDirTest, DataImportTest, FileImportTest, CollectorTemplateTest,
        #            CollectorimportDataTest, CollectorTaskListTest, OperationalMonitoringTest, TaskControlTest, QualityAnalyzeTest,
        #            BloodAnalyzeTest, SchemaAnalyzeTest, FlowManagementTest],
        # 'Cab': [LoginTest, HomePageTest_Cab, OperateDirTest, DataImportTest, FileImportTest, CollectorTemplateTest,
        #            CollectorimportDataTest, CollectorTaskListTest, OperationalMonitoringTest, TaskControlTest, QualityAnalyzeTest,
        #            BloodAnalyzeTest, SchemaAnalyzeTest, FlowManagementTest],
        # 'Cad': [LoginTest, HomePageTest_Cad, OperateDirTest, DataImportTest, FileManagementTest, FileImportTest, CollectorTemplateTest,
        #            CollectorimportDataTest, CollectorTaskListTest, OperationalMonitoringTest, TaskControlTest, QualityAnalyzeTest,
        #            BloodAnalyzeTest, SchemaAnalyzeTest, FlowManagementTest, ProjectDirTest],
        # 'ShuBo': [LoginTest, HomePageTest_Shubo, OperateDirTest, DataImportTest, FileImportTest, CollectorTemplateTest,
        #            CollectorimportDataTest, CollectorTaskListTest, OperationalMonitoringTest, TaskControlTest, QualityAnalyzeTest,
        #            BloodAnalyzeTest, SchemaAnalyzeTest, FlowManagementTest],
        # 'YinPao': [LoginTest, HomePageTest_Yinpao, OperateDirTest, DataImportTest, FileManagementTest, FileImportTest, CollectorTemplateTest,
        #            CollectorimportDataTest, CollectorTaskListTest, OperationalMonitoringTest, TaskControlTest, QualityAnalyzeTest,
        #            BloodAnalyzeTest, SchemaAnalyzeTest, FlowManagementTest, ProjectDirTest],

        'bayMax': [HomePageTest],
        'Beiruan': [OperateDirTest],
        'Beiruan': [OperateDirTestSSSS],
        'Cab': [HomePageTest_Cab],
        'Cad': [HomePageTest_Cad],
        'ShuBo': [HomePageTest_Shubo],
        'YinPao': [HomePageTest_Yinpao],

    }
    cases = map(ParametrizedTestCase.parametrize, Check_module[who])
    for i in cases:
        suite.addTest(i)
    return suite


def runnerCaseApp():

    driver, who = get_driver()
    driver.quit()

    start_time = datetime.now()
    # suite = unittest.TestSuite()

    suite = suite_case(who)

    # suite.addTest(ParametrizedTestCase.parametrize(LoginTest))
    # suite.addTest(ParametrizedTestCase.parametrize(HomePageTest))
    # suite.addTest(ParametrizedTestCase.parametrize(OperateDirTest))
    # suite.addTest(ParametrizedTestCase.parametrize(DataImportTest))
    # suite.addTest(ParametrizedTestCase.parametrize(FileManagementTest))
    # suite.addTest(ParametrizedTestCase.parametrize(FileImportTest))
    # suite.addTest(ParametrizedTestCase.parametrize(CollectorTemplateTest))
    # suite.addTest(ParametrizedTestCase.parametrize(CollectorimportDataTest))
    # suite.addTest(ParametrizedTestCase.parametrize(CollectorTaskListTest))
    # suite.addTest(ParametrizedTestCase.parametrize(OperationalMonitoringTest))
    # suite.addTest(ParametrizedTestCase.parametrize(TaskControlTest))
    # suite.addTest(ParametrizedTestCase.parametrize(QualityAnalyzeTest))
    # suite.addTest(ParametrizedTestCase.parametrize(BloodAnalyzeTest))
    # suite.addTest(ParametrizedTestCase.parametrize(SchemaAnalyzeTest))
    # suite.addTest(ParametrizedTestCase.parametrize(FlowManagementTest))
    # suite.addTest(ParametrizedTestCase.parametrize(ProjectDirTest))


# ---------------- SSSSSSSSSSSSSSSSS--------------------------------
#     suite.addTest(ParametrizedTestCase.parametrize(HomePageTest_SSSS))
#     suite.addTest(ParametrizedTestCase.parametrize(OperateDirTestSSSS))
#     suite.addTest(ParametrizedTestCase.parametrize(DataImportTest_SSSS))
#     suite.addTest(ParametrizedTestCase.parametrize(FileManagementTest_SSSS))
#     suite.addTest(ParametrizedTestCase.parametrize(FileImportTest))
#     suite.addTest(ParametrizedTestCase.parametrize(CollectorTemplateTest_SSSS))
#     suite.addTest(ParametrizedTestCase.parametrize(CollectorimportDataTest_SSSS))
#     suite.addTest(ParametrizedTestCase.parametrize(CollectorTaskListTest_SSSS))
#     suite.addTest(ParametrizedTestCase.parametrize(OperationalMonitoringTest_SSSS))
#     suite.addTest(ParametrizedTestCase.parametrize(TaskControlTest_SSSS))
#     suite.addTest(ParametrizedTestCase.parametrize(QualityAnalyzeTest_SSSS))
#     suite.addTest(ParametrizedTestCase.parametrize(BloodAnalyzeTest))
#     suite.addTest(ParametrizedTestCase.parametrize(SchemaAnalyzeTest))
#     suite.addTest(ParametrizedTestCase.parametrize(FlowManagementTest_SSSS))
#     suite.addTest(ParametrizedTestCase.parametrize(ProjectDirTest_SSSS))
    unittest.TextTestRunner(verbosity=2).run(suite)
    end_time = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((end_time - start_time).seconds) + "秒")

if __name__ == '__main__':
    mk_file()
    # for i in range(100):
    runnerCaseApp()
    writeExcel()
    # send()
