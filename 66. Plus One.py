class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        i = len(digits)-1
        while i >= 0:
            carry += digits[i]
            digits[i] = carry%10
            carry = carry//10
            i-=1
        if carry:
            digits[0] += 1
            digits.append(0)
        return digits