# -*- coding: utf-8 -*-

class ElementParam(object):

    # selenium 关键字
    find_element_by_id = 'id'
    find_element_by_class_name = 'class_name'
    find_element_by_name = 'name'
    find_element_by_xpath = 'xpath'
    find_elements_by_id = 'ids'
    find_elements_by_class_name = 'class_names'
    find_elements_by_xpath = 'xpaths'
    find_elements_by_name = 'names'
    WAIT_TIME = 20  # 查找元素等待时间
    CLICK = 'click'   # 点击事件
    SEND_KEYS = 'send_keys'  # 输入事件
    ACTION_CHAINS = 'action_chains'  # 鼠标悬停事件
    GET_TEXT = 'get_text'
    GET_VALUE = 'get_value'
    MOVE_BY_OFFSET = 'move_by_offset'  # 移动鼠标到某个像素


    # 错误日志
    TIME_OUT = "timeout"
    NO_SUCH = "noSuch"
    WEB_DROVER_EXCEPTION = "WebDriverException"
    INDEX_ERROR = "index_error"
    STALE_ELEMENT_REFERENCE_EXCEPTION = "StaleElementReferenceException"
    DEFAULT_ERROR = "default_error"


    # 检查点
    CONTRARY = "contrary" # 相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
    CONTRARY_GETVAL = "contrary_getval" # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
    DEFAULT_CHECK = "default_check" # 默认检查点，就是查找页面元素
    COMPARE = "compare" # 历史数据和实际数据对比

     # 文件名字
    INFO_FILE = "info.pickle"
    SUM_FILE = "sum.pickle"
    REPORT_FILE = "Report.xlsx"



    URL = 'http://192.168.1.189:8515/#/login'
    #脚本版本
    VERSION = '2019-01-22'


