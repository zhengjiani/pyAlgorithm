"""
最长公共子串
"""
# 滑动窗口法
def getMaxSubStr(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    # 最大公共子串长度
    maxLen = 0
    # 当前重叠子串长度
    tmpMaxLen = 0
    # 最长公共子串结束位置
    maxLenEnd1 = 0
    sb = ""
    i=0
    while i<len1+len2:
        s1begin=s2begin=0
        tmpMaxLen=0
        if i < len1:
            s1begin = len1-i
        else:
            s2begin = i-len1
        j=0
        while (s1begin+j<len1) and (s2begin+j<len2):
            if list(s1)[s1begin] == list(s2)[s2begin]:
                tmpMaxLen += 1
            else:
                if tmpMaxLen > maxLen:
                    maxLen = tmpMaxLen
                    maxLenEnd1 = s1begin + j
                else:
                    tmpMaxLen = 0
            j += 1
        if tmpMaxLen > maxLen:
            maxLen = tmpMaxLen
            maxLenEnd1 = s1begin+j
            i += 1
        i = maxLenEnd1-maxLen
        while i < maxLenEnd1:
            sb = sb+ list(s1)[i]
            i += 1
        return sb

if __name__ == "__main__":
    s1 = "abccade"
    s2 = "dgcadde"
    print(getMaxSubStr(s1,s2))
