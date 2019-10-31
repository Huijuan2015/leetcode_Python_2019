class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        ans = ""
        l1 = len(num1) - 1
        l2 = len(num2) - 1
        if l1 < l2:
            num1, num2 = num2, num1
            l1,l2 = l2, l1
        
        for i, num in enumerate(num1[::-1]):
            idx2 = l2 - i
            if idx2 < 0:
                tmp = carry + int(num)
            else: 
                tmp = carry + int(num) + int(num2[idx2])
            ans = str(tmp%10) + ans
            carry = 1 if (tmp/10 > 0) else 0

        return ans if carry == 0 else str(1) + ans
            
            