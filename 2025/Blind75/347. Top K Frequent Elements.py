import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 第一步：统计每个元素的出现频率
        freq_map = Counter(nums)  # 返回的是一个字典 {num: freq}
        # 例如 nums = [1,1,2,2,3] → freq_map = {1:2, 2:2, 3:1}

        # 第二步：使用最小堆（heap），大小为 k
        # 堆中存储的是 (频率, 元素) 这样的元组
        heap = [] #注意heap定义

        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))  # 把 (频率, 元素) 放进堆
            if len(heap) > k:
                heapq.heappop(heap)  # 如果堆大小超过 k，就移除频率最小的元素

        # 第三步：从堆中取出元素，只保留 num（不需要频率）
        result = []
        while heap:
            freq, num = heapq.heappop(heap)
            result.append(num)

        # 如果题目要求可以按任意顺序返回，可以直接返回
        return result