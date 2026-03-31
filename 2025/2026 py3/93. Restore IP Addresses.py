class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        if len(s) < 4 or len(s) > 12:
            return []
        self.help(s, [], 1)
        return self.res
        
    def help(self, s, ip, n): #n: currently forming which part
        if not s and n > 4:
            self.res.append('.'.join(ip))
        elif n > 4 or not s:
            return
        for i in range(1,4):
            if len(s) >= i:
                part =  s[:i]
                
                if 0<=int(part)<=255 and not (part[0] == '0' and len(part)>1):
                    ip.append(part)
                    self.help(s[i:], ip, n+1)
                    ip.pop() #要记得恢复



