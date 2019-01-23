# -*- coding: utf-8 -*-
from common.ElementParam import ElementParam as ep
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

class OperateElement():

    def __init__(self, driver=''):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def findElement(self, operate):
        try:
            if type(operate) == list:
                for item in operate:
                    t = item['check_time'] if item.get('check_time', 0) != 0 else ep.WAIT_TIME
                    WebDriverWait(self.driver, t).until(lambda x: self.element_by(item))
                return {'result': True}
            if type(operate) == dict:
                '''
                if operate.get('element_info', 0) == 0:
                    return {'result': True}
                如果有元素 yaml文档不要忘记写element_info！！！
                '''
                if operate.get('element_info', 0) == 0: # 如果没有页面元素，就不检测是页面元素，可能是滑动等操作
                    return {'result': True}
                t = operate['check_time'] if operate.get('check_time', 0) != 0 else ep.WAIT_TIME
                el = WebDriverWait(self.driver, t).until(lambda x: self.element_by(operate))
                print('找到了element：', operate['info'])
                print(el)
                return {'result': True}
        except selenium.common.exceptions.TimeoutException:
            return {'result': False, 'type': ep.TIME_OUT}
        except selenium.common.exceptions.NoSuchElementException:
            return {'result': False, 'type': ep.NO_SUCH}
        except selenium.common.exceptions.WebDriverException:
            return {'result': False, 'type': ep.WEB_DROVER_EXCEPTION}
    '''
    {'element_info': 'input-lg', 'find_type': 'class_name', 'operate_type': 'send_keys', 'msg': 'lose1', 'info': '输入用户名lose1'}
    [{'id': 'test001', 'title': '登录失败', 'launch': 1, 'info': '打开testerhome'}]
    <Base.BaseLog.Log object at 0x00000000037F8BA8>
    '''
    def operate(self, operate, testInfo, logTest):
        res = self.findElement(operate)
        print(res)
        if res["result"]:

            return self.operate_by(operate, testInfo, logTest)
        else:
            return res

    def operate_by(self, operate, testInfo, logTest):
        try:
            info = '__%s__%s__%s__%s__' % (operate.get('element_info', ' '), operate.get('find_type', ' '),
                                    operate.get('operate_type', ' '), operate.get('msg', ' '))
            logTest.buildStartLine(str(testInfo[0]['id']) + "__" + testInfo[0]['title']+ "_" + info)
            if operate.get('operate_type', 0) == 0: # 一般为检查点，不需要操作，直接返回true
                print('---------没有找到operate_type在：----应该为检查点-----info为：', operate['info'])
                return {'result': True}
            elements = {
                ep.CLICK: lambda: self.click_opetate(operate),
                ep.SEND_KEYS: lambda: self.send_keys(operate),
                ep.ACTION_CHAINS: lambda: self.action_chains(operate),
                ep.MOVE_BY_OFFSET: lambda: self.move_mouse(operate),
                ep.GET_TEXT: lambda: self.get_text(operate),
                ep.GET_VALUE: lambda: self.get_value(operate)
            }
            return elements[operate['operate_type']]()

        # except IndexError:
        #     logTest.buildStartLine(
        #         testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate["element_info"] + "索引错误")  # 记录日志
        #     # print(operate["element_info"] + "索引错误")
        #     return {"result": False, "type": be.INDEX_ERROR}
        #
        # except selenium.common.exceptions.NoSuchElementException:
        #     logTest.buildStartLine(
        #         testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
        #             "element_info"] + "页面元素不存在或没加载完成")  # 记录日志
        #     # print(operate["element_info"] + "页面元素不存在或没有加载完成")
        #     return {"result": False, "type": be.NO_SUCH}
        # except selenium.common.exceptions.StaleElementReferenceException:
        #     logTest.buildStartLine(
        #         testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
        #             "element_info"] + "页面元素已经变化")  # 记录日志
        #     # print(operate["element_info"] + "页面元素已经变化")
        #     return {"result": False, "type": be.STALE_ELEMENT_REFERENCE_EXCEPTION}
        except KeyError:
            logTest.buildStartLine(
                testInfo[0]['id'] + '__' + testInfo[0]["title"] + "__" + operate[
                     "element_info"] +"__" + 'Operate缺少key, 或者key写错了'
            )
            return {"result": False}
        except Exception as msg:
            logTest.buildStartLine(
                testInfo[0]['id'] + '__' + testInfo[0]["title"] + "__" + operate[
                     "element_info"] +"__" + '没定位的错误' + msg
            )
            return {'result': False}

    # 移动鼠标到某个像素
    def move_mouse(self, operate):
        ActionChains(self.driver).move_by_offset(*tuple(eval(operate['move_to']))).perform()
        return {'result': True}

    # 输入文字操作
    def send_keys(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            print('-----------操作sendkeys之前---------------')
            print(operate['msg'])
            self.element_by(operate).send_keys(operate['msg'])
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            self.element_by(operate)[operate['index']].send_keys(operate['msg'])
        return {'result': True}

    # 点击操作
    def click_opetate(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            self.element_by(operate).click()
            return {'result': True}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            self.element_by(operate)[operate['index']].click()
            return {'result': True}

    #鼠标悬停事件
    def action_chains(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            ActionChains(self.driver).move_to_element(self.element_by(operate)).perform()
            time.sleep(0.7)
            return {'result': True}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            ActionChains(self.driver).move_to_element(self.element_by(operate)[operate['index']]).perform()
            time.sleep(0.7)
            return {'result': True}

    def get_value(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            re_value = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', self.element_by(operate).get_attribute('value'))
            value = ''.join(re_value)
            return {'result': True, 'value': value}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            re_value = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', self.element_by(operate)[operate['index']].get_attribute('value'))
            value = ''.join(re_value)
            return {'result': True, 'value': value}


    def get_text(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', self.element_by(operate).get_attribute('text'))
            text = ''.join(re_reulst)
            return {'result': True, 'text': text}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', self.element_by(operate)[operate['index']].get_attribute('text'))
            text = ''.join(re_reulst)
            return {'result': True, 'text': text}

    # 查找元素的封装
    def element_by(self, operate):
        elements = {
            ep.find_element_by_id: lambda :self.driver.find_element_by_id(operate['element_info']),
            ep.find_element_by_class_name: lambda :self.driver.find_element_by_class_name(operate['element_info']),
            ep.find_element_by_name: lambda : self.driver.find_element_by_name(operate['element_info']),
            ep.find_element_by_xpath: lambda : self.driver.find_element_by_xpath(operate['element_info']),
            ep.find_elements_by_id: lambda: self.driver.find_elements_by_id(operate['element_info']),
            ep.find_elements_by_class_name: lambda : self.driver.find_elements_by_class_name(operate['element_info']),
            ep.find_elements_by_xpath: lambda: self.driver.find_elements_by_xpath(operate['element_info']),
            ep.find_elements_by_name: lambda: self. driver.find_elements_by_name(operate['element_info'])
        }
        return elements[operate['find_type']]()

if __name__=='__main__':
    from common.operate_yaml import getYam
    import os,time
    from common.Logger import myLog
    logTest = myLog.getLog("chrome")
    driver = webdriver.Chrome()
    driver.get('http://192.168.1.189:8515/#/login')
    oe = OperateElement(driver)
    path = os.path.dirname(os.getcwd()) + '\YAML\login\login'
    data = getYam(path)
    print(data)
    for i in data[1]['testcase']:
        oe.operate(i, data[1]['testinfo'], logTest)
        print(i['info'])
        # time.sleep(3)



