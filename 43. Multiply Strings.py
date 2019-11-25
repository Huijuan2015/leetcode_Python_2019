class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        res = [0 for _ in range(m+n)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                res[i+j+1] += int(num1[i]) * int(num2[j])
                res[i+j] += res[i+j+1]/10
                res[i+j+1] %= 10
                
        i = 0
        while i < len(res) and res[i] == 0:
            i+=1
        s = "".join([str(ch) for ch in res[i:]])
        return s if s else '0'



`num1[i] * num2[j]` will be placed at indices `[i + j`, `i + j + 1]` 

https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation