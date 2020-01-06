class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        res = []
        cnt = collections.Counter(nums)
        # for k, v in sorted(cnt.items(), key=lambda item:item[1], reverse=True)[:k]:
        #     print k,v
        #     res.append(k)
        
        return [key for key,val in sorted(cnt.items(), key=lambda item:item[1], reverse=True)[:k]]
        