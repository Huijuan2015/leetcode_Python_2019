O(sqrtn)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 1
        while i * i <= x:
            if i * i == x:
                return i
            i += 1
        return i-1

Olgn-faster
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 0
        end = x
        while start <= end:
            mid = start + (end - start)/2

            if mid*mid == x:
                return mid
            if mid*mid>x and (mid-1)*(mid-1)<x:
                return mid - 1
            elif mid*mid < x:
                start = mid + 1
            else:
                end = mid - 1



class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        #mid = -1
        if x < 2:
            return x
        while left < right:
            mid = (left+right)/2
            if x/mid >= mid:
                left = mid+1
            else:
                right = mid
            #print mid
        return right - 1
