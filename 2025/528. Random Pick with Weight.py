class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total_sum = total  

    def pickIndex(self):
        """
        :rtype: int
        """
        # 返回下标 i 的概率应该与 w[i] / sum(w) 成比例。
        rand = random.randint(1, self.total_sum)

        # 在 prefix_sums 中找到第一个 ≥ rand 的位置
        # return bisect.bisect_left(self.prefix_sums, rand)
        for i, psum in enumerate(self.prefix_sums):
            if rand <= psum:
                return i

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()