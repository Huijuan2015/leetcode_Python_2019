class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []
        res = []
        nums.sort() # 先排序
        for i in range(len(nums)-2):
            # 跳过重复的第一数
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # 跳过重复的第二数和第三数
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res





class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # need better solution
        nums.sort()
        res = []

        for i in xrange(len(nums)):
            target = -nums[i]
            start = i + 1
            end  = len(nums) - 1

            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue #[-1,-1,0,1,2,4]去除第二个相同的-1作为第一个数
            while start < end:
                first = nums[i]
                second = nums[start]
                third = nums[end]

                if second + third < target and start < end:
                    start += 1
                else:
                    end -= 1
                if second + third == target:
                    res.append([first, second, third])

                    while start < end and nums[start] == second:
                        start += 1
                    while start < end and nums[end] == third:
                        end -= 1
        return res