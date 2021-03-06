class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 求sub sum， 求余数，如果2个余数一样，说明中间的部分符合题目要求
        mp = {} #余数：idx
        sum = [0 for _ in range(len(nums))]
        sumUp = 0
        mp[0] = -1#? 要初始化加一个最开始的sum，以防止结果是从idx0开始的片段， ex [0,0] find 0
        
        for i in range(len(nums)):
            sumUp += nums[i]
            sum[i] = sumUp
            if k == 0:
                remain = sum[i]
            else:
                remain = sum[i]%k
            if remain in mp:
                if i-mp[remain] > 1:
                    return True  
            else:
                mp[remain] = i 
                
        return False
        

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum = [0 for _ in range(len(nums))]
        remainMap = {}
        remainMap[0] = -1   加入0很重要
        for i in range(len(nums)):
            sum[i] += nums[i]
            if i-1 >= 0:
                sum[i] += sum[i-1]
            remain = sum[i]
            if k != 0:
                remain = sum[i] % k
            if remain in remainMap:
                if i - remainMap[remain] > 1:
                    return True
            else:
                remainMap[remain] = i
        print sum, remainMap
        return False
            
            