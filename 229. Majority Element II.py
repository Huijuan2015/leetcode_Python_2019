class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 2 at most
        if not nums:
            return []
        
        candidate1, candidate2 = None, None
        cnt1, cnt2 = 0, 0
        for num in nums:
            if candidate1 == num:
                cnt1 += 1
            elif candidate2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                candidate1 = num
                cnt1 = 1
            elif cnt2 == 0:
                candidate2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
                # if cnt1 > 1:
                #     cnt1 -= 1
                # elif cnt2 > 1:
                #     cnt2 -= 1
            # print cnt1, candidate1, cnt2, candidate2
        # return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums)//3]
        res = []
        # print cnt1, cnt2
        if nums.count(candidate1)>len(nums)//3:  不能用cnt1,cnt2, 因为不是完全count     
            res.append(candidate1)
        if nums.count(candidate2)>len(nums)//3:           
            res.append(candidate2)
        return res