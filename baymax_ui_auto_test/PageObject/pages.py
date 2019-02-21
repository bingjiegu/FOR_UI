from common.operate_element import OperateElement
from common.ErrorInfo import get_error_info
from common.ElementParam import ElementParam
from PageObject.CountResult import count_result
from time import sleep
import os
from common.Operate_str import *
import time
from common.OperateFile import new_download_file_mtime

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class PagesObjects:

    def __init__(self, kwargs):
        self.driver = kwargs['driver']              # driver
        if kwargs['testmsg'][1]['testinfo'][0].get('launch', 0) == 0:           # 刷新当前页面
            print('=======================================刷新了页面========================================')
            self.driver.refresh()

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
            # 生成随机的send_keys的值
            if str(i.get('msg', 'aaaaaaa'))[-4:] == '+随机数':
                i['msg'] = random_str(i['msg'])
                self.get_value.append(i['msg'])
            if i.get('element_info', 'aaaaaa')[-4:] == '+随机数':
                if i['find_type'] == 'name':
                    i['element_info'] = self.get_value[int(i['v_index'])]
                if i['find_type'] == 'xpath':
                    i['element_info'] = i['element_info'][: -4] % self.get_value[int(i['v_index'])]
            if i.get('element_info', 'aaaaaa')[-3:] == '+拼接':
                if i['find_type'] == 'name':
                    i['element_info'] = self.get_value[int(i['v_index'])] + i['join_value']
                if i['find_type'] == 'xpath':
                    i['element_info'] = i['element_info'][: -3] % (self.get_value[int(i['v_index'])] + i['join_value'])

            result = self.operateElement.operate(i, self.testInfo, self.logTest)
            if not result['result']:
                msg = get_error_info({'type': ElementParam.DEFAULT_ERROR, 'element_info': i['element_info']})
                self.testInfo[0]['msg'] = msg
                self.isOperate = False
                return False
            if i.get('is_time', 0) != 0:
                sleep(i['is_time'])
            if i.get('operate_type', 0) == ElementParam.GET_TEXT or i.get('operate_type', 0) == ElementParam.GET_VALUE or i.get('operate_type', 0) == ElementParam.GET_ATTR:
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
                if i.get('element_info', 'aaaaaa')[-4:] == '+随机数':
                    if i['find_type'] == 'name':
                        i['element_info'] = self.get_value[int(i['v_index'])]
                    if i['find_type'] == 'xpath':
                        i['element_info'] = i['element_info'][: -4] % self.get_value[int(i['v_index'])]
                if i.get('element_info', 'aaaaaa')[-3:] == '+拼接':
                    if i['find_type'] == 'name':
                        i['element_info'] = self.get_value[int(i['v_index'])] + i['join_value']
                    if i['find_type'] == 'xpath':
                        i['element_info'] = i['element_info'][: -3] % (self.get_value[int(i['v_index'])] + i['join_value'])
                op_re = self.operateElement.operate(i, self.testInfo, self.logTest)
                # 默认检查点，检查元素存在
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.DEFAULT_CHECK and not op_re['result']:
                    msg = get_error_info({"type": ElementParam.DEFAULT_CHECK, "element_info": i['element_info'], "info": i['info']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    return result
                # 检查 元素不存在
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.CONTRARY and op_re['result']:
                    msg = get_error_info({'type': ElementParam.CONTRARY, 'element': i['element_info'], 'info': i['info']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查前面页面的值 与后面页面某值相等
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.COMPARE and self.is_get and op_re['text'] not in self.get_value[i['attr_index']]:
                    msg = get_error_info({'type': ElementParam.COMPARE, 'history': self.get_value, 'info': i['info'], 'current': op_re['text']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                 # 检查前面页面的值 与后面页面某值不相等
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.CONTRARY_GETVAL and self.is_get and op_re['text'] in self.get_value[i['attr_index']]:
                    msg = get_error_info({'type': ElementParam.CONTRARY_GETVAL, 'history': self.get_value, 'info': i['info'], 'current': op_re['text']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查当前页面的URL与预期的地址相等
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.URL_INEQUALITY_ERROR and op_re['url'] != ElementParam.HOST + i.get('url', 'ooo'):
                    msg = get_error_info({'type': ElementParam.URL_INEQUALITY_ERROR, 'info': i['info'], 'get_url': op_re['url'], 'expect_url': ElementParam.HOST + i.get('url', 'ooo')})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查当前页面的URL是否包含预期的url
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.URL_CONTAIN and (ElementParam.HOST + i.get('url', 'ooo')) not in op_re['url']:
                    msg = get_error_info({'type': ElementParam.URL_CONTAIN, 'info': i['info'], 'get_url': op_re['url'], 'expect_url': ElementParam.HOST + i.get('url', 'ooo')})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查当前页面的属性值等于预期的值 如果不相等就返回False
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.EXPECT_VALUE_EQUAL and op_re['text'] != i.get('expect_value', 'ooo'):
                    msg = get_error_info({'type': ElementParam.EXPECT_VALUE_EQUAL, 'info': i['info'], 'get_attr': op_re['text'], 'expect_value': i.get('expect_value', 'ooo')})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查前面页面是属性值不包含预期的属性值 如果包含就返回False
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.ATTR_NOT_CONTAIN and self.is_get \
                        and contain_str(i['attr_value'], self.get_value, i.get('attr_index', 0)):
                    msg = get_error_info({'type': ElementParam.ATTR_NOT_CONTAIN, 'history': self.get_value, 'info': i['info'], 'current': i['attr_value']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查前面页面获取的属性值 包含预期的属性值  如果不包含就返回False
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.ATTR_CONTAIN and self.is_get \
                        and contain_not_str(i['attr_value'], self.get_value, i.get('attr_index', 0)):
                    msg = get_error_info({'type': ElementParam.ATTR_CONTAIN, 'history': self.get_value, 'info': i['info'], 'current': i['attr_value']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查页面元素显示  如果 不显示就返回False
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.DISPLAYED and not op_re['result']:
                    msg = get_error_info({'type': ElementParam.DISPLAYED, 'info': i['info'], 'element': i['element_info']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查页面元素不显示  如果 显示就返回False
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.NOT_DISPLAYED and op_re['result']:
                    msg = get_error_info({'type': ElementParam.NOT_DISPLAYED, 'info': i['info'], 'element': i['element_info']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查有没有成功下载文件
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.IS_DOWNLOAD and (time.time() - new_download_file_mtime()) > 5:
                    msg = get_error_info({'type': ElementParam.IS_DOWNLOAD,  'info': i['info'], 'd_timeout': i['d_timeout']})
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