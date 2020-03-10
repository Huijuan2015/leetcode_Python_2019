class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        num = 0
        curr = ''
        for ch in s:
            print stk, curr, num
            if ch == '[':
                stk.append(curr)
                stk.append(num)
                curr = ''
                num = 0
            elif ch == ']':
                n = stk.pop()
                prev = stk.pop()
                curr = prev + n*curr
            elif ch.isdigit():
                num = num*10+int(ch)
            else:
                curr += ch
        return curr
                
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk, currStr, num = [], "", 0
        for ch in s:
            if ch == '[':
                stk.append(currStr)
                stk.append(num)
                currStr, num = "", 0
            elif ch == ']':
                n, prev = stk.pop(), stk.pop()
                currStr = prev + n*currStr
            elif ch.isdigit():
                num = num*10 + int(ch)
            else:
                currStr += ch
        return currStr
                
        
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        
        for i in range(len(s)):
            if s[i] != ']':
                stk.append(s[i])
                continue
            else:
                curr = ""
                while stk and stk[-1] != '[':
                    curr += stk.pop()
                stk.pop()
                # get string 
                curr = curr[::-1]
                # get number
                n = ""
                while stk and stk[-1] in "0123456789":
                    n += stk.pop()
                curr *= int(n[::-1])
                stk += list(curr)
        return "".join(stk)