class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # i = len(digits) - 1
        # carry = 0
        # while i >= 0:
        #     carry += digits[i]
        #     digits[i] = carry % 10
        #     carry =  carry/10
        #     i -= 1
        # if carry:
        #     #999 + 1 = 100 + 0
        #     digits[0] += 1
        #     digits.append(0)
        # return digits

        # solution2: 
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        # return [1] + digits
        digits.insert(0,1)
        return digits

