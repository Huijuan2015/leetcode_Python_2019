class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.helper(s, 0, "", [], 0)
        return self.res
    
    def valid(self, s):
        if int(s) <= 255 and int(s) >= 0:
            return True
        return False
    
    def helper(self, s, idx, carry, path, segs): #path is a list
        # stop
        # print idx, carry, path
        if segs > 4:
            return
        if idx == len(s) and not carry and segs == 4:
            self.res.append('.'.join(path))
            return
        if idx == len(s) or not self.valid(carry+s[idx]):
            return
        # s, 0, carry curr idx
        curr = carry+s[idx]
        if len(curr) > 1 and curr[0] == '0':
            return
        if self.valid(curr):
            # continue carry
            self.helper(s, idx+1, curr, path,segs)
            # not carry, append
            self.helper(s, idx+1, "", path+[curr],segs+1)
            
        