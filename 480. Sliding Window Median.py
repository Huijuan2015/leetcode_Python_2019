Time: O(n)
Space: O(1)
nk?

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        #bisect
        if k == 0:
            return []
        
        window = sorted(nums[:k]) # length k
        res = []
        for i in range(k, len(nums)+1):
            # 求med
            med = (window[k//2] +window[(k-1)//2])/2.0
            res.append(med)
            if i == len(nums): break
            # 求位置 nums[i-k] 在window中删除
            idx = bisect.bisect_left(window, nums[i-k]) #如果要插入第一个数的位置就是所求位置
            window.pop(idx)
            #new window
            bisect.insort_left(window, nums[i])
        return res

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        # brute force tle
        
        i, j  = 0, 0 
        window = [] # length k
        heapq.heapify(window)
        res = []
        while j < len(nums):
            if len(window) < k:
                heapq.heappush(window, nums[j])
            if len(window) == k:
                if k % 2 == 0:
                    # print window, nums[i]
                    tmp = float(heapq.nsmallest(k/2, window)[-1] + heapq.nsmallest(k/2+1, window)[-1])/2
                    res.append(tmp)
                else:
                    res.append(heapq.nsmallest(k/2+1, window)[-1])
                window.remove(nums[i])
                i += 1
                
            j += 1
        return res