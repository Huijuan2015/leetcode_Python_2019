class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #边填充map边找
        prefix_sum_cnt = defaultdict(int) # sum not include current index, {sum : cnt}
        prefix_sum_cnt[0] = 1
        prefix_sum = 0
        count  = 0
        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in prefix_sum_cnt:
                count += prefix_sum_cnt[prefix_sum - k]
            prefix_sum_cnt[prefix_sum] += 1
        return count

            

        