class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i-1]
            # print self.w #求份数总和

    def pickIndex(self):
        """
        :rtype: int
        """
        val = random.randint(1, self.w[-1])
        # return bisect.bisect_left(self.w, val)
        
        #binary search
        start = 0
        end = len(self.w)-1

        while start < end:
            mid = (start + end)//2
            if val <= self.w[mid]:
                end = mid
            else:
                start = mid+1
        return start
        
/////       
def __init__(self, w):
        self.w = list(itertools.accumulate(w))

    def pickIndex(self):
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()