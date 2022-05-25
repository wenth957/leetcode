
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen = len(s)
        plen = len(p)
        # 递归终止条件
        if plen == 0:
            return s == ''
        elif plen == 1:
            return slen == 1 and (p[0] == s[0] or p[0] == '.')
        # 单次递归逻辑
         # 下个字符不是*的情况，匹配完成...直接继续
        elif plen > 1 and p[1] != '*':
            if s and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            # 如果下一个字符不是*，不等于直接返回false
            return False
        elif plen > 1 and p[1] == '*':
            if s and (p[0] == s[0] or p[0] == '.'):
                #  匹配完成...进入下次匹配...
                #  *匹配0个即直接跳过下一个*号去匹配
                #  *匹配多个即用s+i继续取匹配p[0]
                #  直到不相等，两条递归路径合并
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            # 不满足相等条件时，如果下个是*，可以匹配0个该字符，仍然可能匹配
            return self.isMatch(s, p[2:])


s = Solution()
print(s.isMatch("aa", "b*a*"))
