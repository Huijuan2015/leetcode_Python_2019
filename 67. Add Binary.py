class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        #return bin(int(a, 2) + int(b, 2))[2:]
        # for i in xrange(len(a)-1, -1, -1):
        res = ''
        i, j, plus = len(a)-1, len(b)-1, 0
        while i >= 0 or j >= 0 or plus == 1:
            plus += int(a[i]) if i >=0 else 0
            plus += int(b[j]) if j >=0 else 0
            res = str(plus%2)+res
            i,j,plus = i-1,j-1,plus/2
        return res

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j, carry = len(a) - 1, len(b) - 1, 0
        res = ""
        
        while i >= 0 or j >= 0 or carry == 1:
            tmp = 0
            tmp += int(a[i]) if i>= 0 else 0
            tmp += int(b[j]) if j>= 0 else 0
            tmp += carry
            res = str(tmp%2) + res
            carry = tmp/2
            i -= 1
            j -= 1
        return res
    