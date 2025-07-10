class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 要转！！！
        s = list(s) # 将字符串转为列表，方便修改
        stk = []
        for i in range(len(s)):
            if s[i] == '(': # 字母
                stk.append(i)
            elif s[i] == ')': # 处理多余的右括号)
                if stk:
                    stk.pop()
                else:
                    s[i] = ''
        while stk: # 处理多余的左括号 (
            s[stk.pop()] = ''
        return ''.join(s) #链接！！！