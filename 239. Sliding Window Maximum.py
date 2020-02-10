class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []
        n = len(nums)
        if k == 1:
            return nums
        res = []
        dq = collections.deque()
        maxIdx = 0
        
        def cleandq(i): # popleft and remove all smaller than current i
            if dq and dq[0] == i-k:
                dq.popleft()
            while dq and nums[i] > nums[dq[-1]]: #把队列中当前更小的值都pop，留下队首就是最大
                dq.pop()
            
        for i in range(k):
            cleandq(i)
            dq.append(i)
            if nums[i] > nums[maxIdx]:
                maxIdx = i
        res.append(nums[maxIdx])
    
        
        for i in range(k, n):
            # print dq, i
            cleandq(i)
            dq.append(i)
            res.append(nums[dq[0]])
        return res

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        
        window = sorted(nums[:k]) # length k
        res = []
        for i in range(k, len(nums)+1):
            # 求med
            # med = (window[k//2] +window[(k-1)//2])/2.0
            res.append(window[-1])
            if i == len(nums): break
            # 求位置 nums[i-k] 在window中删除
            idx = bisect.bisect_left(window, nums[i-k]) #如果要插入第一个数的位置就是所求位置
            window.pop(idx)
            #new window
            bisect.insort_left(window, nums[i])
        return res