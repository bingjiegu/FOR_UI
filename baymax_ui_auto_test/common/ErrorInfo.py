from common.ElementParam import ElementParam

def get_error_info(kw):
    elements ={
        ElementParam.CONTRARY: lambda: "==检查点_%s失败_%s依然在页面==" % (kw["info"], kw["element"]),
        ElementParam.DEFAULT_CHECK: lambda: "==检查点_%s失败，请检查_%s==" % (kw["info"], kw["element_info"]),
        ElementParam.COMPARE: lambda: "==检查点___info:_%s___对比数据失败，当前取到的数据为:%s,历史取到数据为:%s" % (kw["info"], kw["current"], kw["history"]),
        ElementParam.CONTRARY_GETVAL: lambda: "==检查点____info:_%s___对比数据失败，当前取到的数据为:%s,历史取到数据为:%s" % (kw["info"], kw["current"], kw["history"]),
        ElementParam.ATTR_NOT_CONTAIN: lambda: "==检查点____info:_%s___对比属性值失败，前面获取的属性值包含预期属性值，"
                                               "当前取到的数据为:%s,历史取到数据为:%s" % (kw["info"], kw["current"], kw["history"]),
        ElementParam.ATTR_CONTAIN: lambda: "==检查点____info:_%s___对比属性值失败，前面获取的属性值不包含预期属性值，"
                                               "当前取到的数据为:%s,历史取到数据为:%s" % (kw["info"], kw["current"], kw["history"]),
        ElementParam.DISPLAYED: lambda: "==检查点____info:_%s___element:__%s__没有在页面显示" % (kw["info"], kw["element"]),
        ElementParam.NOT_DISPLAYED: lambda: "==检查点____info:_%s___element:__%s__在页面显示了" % (kw["info"], kw["element"]),
        ElementParam.URL_INEQUALITY_ERROR: lambda : '预期的URL: %s 不等于获取的URL: %s'% (kw['expect_url'], kw['get_url']),
        ElementParam.DEFAULT_ERROR: lambda: '请检查%s是否存在' % kw['element_info'],
    }
    return elements[kw['type']]()