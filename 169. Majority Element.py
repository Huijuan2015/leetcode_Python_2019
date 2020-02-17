class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != major:
                cnt -= 1
                if cnt == 0:
                    major, cnt = nums[i], 1
            else:
                cnt += 1
        return major if cnt > 0 else None


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num==candidate else -1)
        return candidate