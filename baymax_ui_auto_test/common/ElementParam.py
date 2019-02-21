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
    GET_CURRENT_URL = 'get_current_url'
    GET_ATTR = 'get_attr'
    IS_DISPLAYED = "is_displayed"  # 检查元素是否显示
    FIND_DOWN = "find_down"  # 下拉菜单中向下查找元素
    MOVE_SCROLLBAR_BOTTOM = "move_scrollbar_bottom"  # 移动滚动条到某元素底部
    UPLOAD_FILE = "upload_file"  # 上传文件 使用autoit可执行文件


    # 错误日志
    TIME_OUT = "timeout"
    NO_SUCH = "noSuch"
    WEB_DROVER_EXCEPTION = "WebDriverException"
    INDEX_ERROR = "index_error"
    STALE_ELEMENT_REFERENCE_EXCEPTION = "StaleElementReferenceException"
    DEFAULT_ERROR = "default_error"
    URL_INEQUALITY_ERROR = "url_inequality_error"  # URL不相等错误


    # 检查点
    CONTRARY = "contrary"  # 相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
    CONTRARY_GETVAL = "contrary_getval"  # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
    DEFAULT_CHECK = "default_check"  # 默认检查点，查找页面元素是否存在
    COMPARE = "compare"  # 历史数据和实际数据对比
    ATTR_NOT_CONTAIN = "attr_not_contain"  # 历史属性值不包含某值
    ATTR_CONTAIN = "attr_contain"  # 历史属性值包含某值
    DISPLAYED = "displayed"  # 检查元素显示
    NOT_DISPLAYED = "not_displayed"  # 检查元素不显示
    EXPECT_VALUE_EQUAL = "expect_value_equal" #当前页面的任意类型（text\value\其他属性）的属性值 是否符合预期值
    IS_DOWNLOAD = 'is_download'  # 检查是否成下载了任务
    URL_CONTAIN = "url_contain"  # 获取的url包含预期的url

    # 文件名字
    INFO_FILE = "info.pickle"
    SUM_FILE = "sum.pickle"
    REPORT_FILE = "Report.xlsx"


    URL = 'http://192.168.1.189:8515/#/login'

    HOST = 'http://192.168.1.189:8515'
    #脚本版本
    VERSION = '2019-02-21'


