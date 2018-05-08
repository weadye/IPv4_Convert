def convert_ipv4(sAddress):
    iResult = 0
    str = ''
    i = 1
    bLastIsSpace = False
    bAfterDot = False
    setNumbers = set(['0','1','2','3','4','5','6','7','8','9'])
    for s in sAddress:
        if s == ' ':
            bLastIsSpace = True
        elif (not bAfterDot) and bLastIsSpace and (s != ' ' and s != '.'):
            raise NameError('Error spaces')
        elif bAfterDot and s == ' ':
            bAfterDot = True
        elif s == '.':
            bLastIsSpace = False
            bAfterDot = True
            if str == '':
                raise NameError('Each address number should not be null')
            if len(str) > 3:
                raise NameError('Each address number should be 3-digits')
            iStr = int(str)
            if iStr > 255 :
                raise NameError('Each address number should in [0,255]')
            iResult = iResult << 8 ^ iStr
            i += 1
            str = ''
        elif s not in setNumbers:
            raise NameError('Each number should in [0-9]')
        else :
            bLastIsSpace = False
            bAfterDot = False
            str += s
    iResult = iResult << 8 ^ int(str)
    if i != 4:
        raise NameError('Invalid format of string, please make sure 4 address numbers are given')
    return iResult

