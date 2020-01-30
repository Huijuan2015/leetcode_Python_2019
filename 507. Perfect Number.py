class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        sum = 0
        i = 1
        while i*i <= num:
            if num%i == 0:
                sum += i
                if (i*i) != num:
                    sum += num/i
            i+=1
                    
        return sum-num == num