

def contain_str(current='', history=[], att_index=0):
    try:
        att_index = int(att_index)
        result = list(map(str, history))
        if current in result[att_index]:
            return True
        else:
            return False
    except IndexError:
        print('++++++++++++索引错误++++++++++++++++++')
        return True

def contain_not_str(current='', history=[], attr_index=0):
    try:
        att_index = int(attr_index)
        result = list(map(str, history))
        if current in result[att_index]:
            return False
        else:
            return True
    except IndexError:
        print('++++++++++++索引错误++++++++++++++++++')
        return True


if __name__ == "__main__":
    a = ['bbbaaaddd', True]
    b = 'True'
    c = 'sdfsd'
    print(contain_str(b, a))
    print(contain_not_str(c, a, '2'))