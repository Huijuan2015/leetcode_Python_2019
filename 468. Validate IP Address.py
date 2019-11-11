class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        # s = "123"
        if IP.count(".") == 3:
            return "IPv4" if self.valid4(IP.split('.')) else "Neither"
        elif IP.count(":") == 7:
            return "IPv6" if self.valid6(IP.split(':')) else "Neither"
        return "Neither"
    
    def valid4(self, list):
        if not list:
            return 
        for l in list:
            if not l:
                return False
            if not l.isdigit() or int(l) > 255 or (len(l)>1 and int(l[0]) == 0):
                return False
        return True
    
    def valid6(self, list):
        if not list:
            return False
        for l in list:
            if not l:
                return False
            if len(l) > 4:
                return False
            for i in l:
                if i not in "0123456789abcdefABCDEF":
                    return False
                
        if list[0][0] not in "123456789abcdefABCDEF":
            return False
        return True