from common.ElementParam import ElementParam

def get_error_info(kw):
    elements ={
        ElementParam.DEFAULT_ERROR: lambda: '请检查%s' % kw['element_info']
    }
    return elements[kw['type']]()