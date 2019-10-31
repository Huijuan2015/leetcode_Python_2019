class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # clean code
        carry = 0
        ans = ""
        i = len(num1) - 1
        j = len(num2) - 1
        
        while i >= 0 or j >= 0 or carry:
            tmp = 0
            tmp += int(num1[i]) if i >= 0 else 0
            tmp += int(num2[j]) if j >= 0 else 0
            tmp += carry
            ans = str(tmp%10) + ans
            carry = tmp/10
            i, j = i-1, j-1
        return ans
    
    #first try
#         carry = 0
#         ans = ""
#         l1 = len(num1) - 1
#         l2 = len(num2) - 1

#         if l1 < l2:
#             num1, num2 = num2, num1
#             l1,l2 = l2, l1
#         # better use reverse order so that can make it 1 for loop
#         for i, num in enumerate(num1[::-1]):
#             idx2 = l2 - i
#             if idx2 < 0:
#                 tmp = carry + int(num)
#             else: 
#                 tmp = carry + int(num) + int(num2[idx2])
#             ans = str(tmp%10) + ans # use another for loop outside if not use str
#             carry = 1 if (tmp/10 > 0) else 0

#         return ans if carry == 0 else str(1) + ans

            
            