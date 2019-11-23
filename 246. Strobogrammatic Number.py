class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # 6-9 8-8 0-0

        mp = {'0':'0','6':'9','8':'8', '9':'6', '1':'1'}
        res = ""
        for n in num:
            if n not in mp:
                return False
            res = mp[n] + res
            # print res
        return res == num