class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, prev, curr = 0, -1, 0 #prev length
        
        for num in nums:
            if num == 0:
                prev = curr
                curr = 0
            else:
                curr += 1
            ans = max(ans, curr+prev+1)
        return ans

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, curr, prev = 0, 0, -1 # prev index
        for i, num in enumerate(nums):
            if num == 1:
                curr += 1
            else:
                curr = i-prev
                prev = i
            ans = max(ans, curr)
        return ans
       
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flip = 1
        ans = 0
        curr = 0
        prev = -1# prev index
        for i, num in enumerate(nums):
            # print curr, prev
            if num == 1:
                curr += 1
            elif flip:
                prev = i
                flip -= 1
                curr += 1
            else:
                curr = i-prev
                flip = 0
                prev = i
            ans = max(ans, curr)
        return ans