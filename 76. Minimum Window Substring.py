class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #left right cnt-- minlen
        #扩展right： mp > 0: right++, mp ++, cnt --
        #确定解： cnt = 0
        #缩小left 到count>0
        import collections
        mp = collections.Counter(t)
        left, right, cnt, minLen = 0, 0, len(t), float('inf')
        res = ""
        while right < len(s) or cnt == 0:
            #print left, right, cnt
            if cnt == 0:
                if minLen > right-left+1:
                    minLen = right-left+1
                    res = s[left:right]
                #print s[left], mp[s[left]], left, right, cnt
                if mp[s[left]] >= 0:
                    cnt += 1
                mp[s[left]]+= 1
                left += 1
                # cnt += 1
            else:
                if mp[s[right]] >= 1:
                    cnt -= 1
                mp[s[right]] -= 1
                right += 1   
        return res
了解了第一道题目以后，这道题目也很容易思考出来。解题时，按照步骤：

扩展窗口，窗口中包含一个T中子元素，count–；
通过count或其他限定值，得到一个可能解。
只要窗口中有可能解，那么缩小窗口直到不包含可能解。

首先，维护一个map，一个窗口。先看右边界，当窗口扩展包含全部ABC时停下，这个时候必然有count == 0。
但是，这个时候的结果字符串可能很长，所以我们要接着缩小左边界。同时，当count == 0时，我们要一直缩小左边界以找到更短的字符串。
慢慢count>0了，表明窗口中不包含全部的T了，那么又要扩展窗口。依次类推，最终找到最短字符串。
套用模板
