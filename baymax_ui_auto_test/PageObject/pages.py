from common.operate_element import OperateElement
from common.ErrorInfo import get_error_info
from common.ElementParam import ElementParam
from PageObject.CountResult import count_result
from time import sleep
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class PagesObjects:

    def __init__(self, kwargs):
        self.driver = kwargs['driver']              # driver
        if kwargs.get('launch', 0) == 0:           # 刷新当前页面
            self.driver.get(self.driver.current_url)

        self.operateElement = ""   # 操作元素的手柄
        self.isOperate = True     # 一个开关  默认为True operate失败时改为False  结果校验时 判断这个值为True就进行判断， 是False就不用校验结果
        self.testmsg = kwargs['testmsg']   # yaml读取的数据值
        self.logTest = kwargs['logTest']   # log对象 可以进行写log操作
        self.testInfo = kwargs['testmsg'][1]['testinfo']  # 用例的基本信息
        self.testcase = kwargs['testmsg'][1]['testcase']  # 元素的基本信息
        self.testcheck = kwargs['testmsg'][1]['check']  # 校验的基本信息
        self.caseName = kwargs['caseName']           # 用例的方法名称，unittest框架中的 test开头的方法名称
        self.get_value = []
        self.is_get = False

    def operate(self):
        if self.testmsg[0] is False:
            self.isOperate = False
            return False
        self.operateElement = OperateElement(self.driver)
        for i in self.testcase:
            result = self.operateElement.operate(i, self.testInfo, self.logTest)
            if not result['result']:
                msg = get_error_info({'type': ElementParam.DEFAULT_ERROR, 'element_info': i['element_info']})
                self.testInfo[0]['msg'] = msg
                self.isOperate = False
                return False
            if i.get('is_time', 0) != 0:
                sleep(i['is_time'])
            if i.get('operate_type', 0) == ElementParam.GET_TEXT or i.get('operate_type', 0) == ElementParam.GET_VALUE:
                self.get_value.append(result['text'])
                self.is_get = True
        return True

    def checkPoint(self):
        result = self.check()
        count_result(result=result, testcase=self.testcase, testcheck=self.testcheck, testinfo=self.testInfo,
                     name='chrome', case_name=self.caseName, logTest=self.logTest, driver=self.driver)

    def check(self):
        result = True
        if self.isOperate:
            for i in self.testcheck:
                op_re = self.operateElement.operate(i, self.testInfo, self.logTest)
                # 默认检查点，检查元素存在
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.DEFAULT_CHECK and not op_re['result']:
                    msg = get_error_info({"type": ElementParam.DEFAULT_CHECK, "element_info": i['element_info'], "info": i['info']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    return result
                # 检查 元素不存在
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.CONTRARY and op_re[result]:
                    msg = get_error_info({'type': ElementParam.CONTRARY, 'element': i['element_info'], 'info': i['info']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查前面页面的值 与后面页面某值相等
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.COMPARE and self.is_get and op_re['text'] not in self.get_value:
                    msg = get_error_info({'type': ElementParam.COMPARE, 'element_info': i['element_info'], 'info': i['info'], 'history': op_re['text']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                 # 检查前面页面的值 与后面页面某值相等
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.CONTRARY_GETVAL and self.is_get and op_re['text'] in self.get_value:
                    msg = get_error_info({'type': ElementParam.CONTRARY_GETVAL, 'element_info': i['element_info'], 'info': i['info'], 'history': op_re['text']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查当前页面的URL与预期的地址相等
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.GET_CURRENT_URL and op_re['url'] != ElementParam.HOST + i.get('url', 'ooo'):
                    msg = get_error_info({'type': ElementParam.URL_INEQUALITY_ERROR, 'info': i['info'], 'get_url': op_re['url'], 'expect_url': ElementParam.HOST + i.get('url', 'ooo')})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
        else:
            result = False
        return result


if __name__ == "__main__":
    from selenium import webdriver
    from common.Logger import myLog
    from common.operate_yaml import getYaml
    driver = webdriver.Chrome()
    driver.get('http://192.168.1.189:8515/#/login')
    logTest = myLog.getLog("chrome")
    testmsg = getYaml(PATH('../YAML/login/login'))
    kw = {'driver': driver, 'logTest': logTest, 'testmsg': testmsg}
    po = PagesObjects(kw)
    a = po.operate()
    print('aaaaaaaa::', a)