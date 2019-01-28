from common.ElementParam import ElementParam

def get_error_info(kw):
    elements ={
        ElementParam.DEFAULT_ERROR: lambda: '请检查%s' % kw['element_info'],
        ElementParam.URL_INEQUALITY_ERROR: lambda : '预期的URL: %s 不等于获取的URL: %s'% (kw['expect_url'], kw['get_url'])
    }
    return elements[kw['type']]()