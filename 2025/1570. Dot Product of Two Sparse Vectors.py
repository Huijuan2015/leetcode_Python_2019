class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # 只存非 0 的值
        self.data = {}
        for i, val in enumerate(nums):
            if val != 0:
                self.data[i] = val
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0
        if len(vec.data) > len(self.data):
            for i in self.data:
                if i in vec.data:
                    res += (self.data[i] * vec.data[i])
        else:
            for i in vec.data:
                if i in self.data:
                    res += (self.data[i] * vec.data[i])
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)