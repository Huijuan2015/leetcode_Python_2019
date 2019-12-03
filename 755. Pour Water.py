class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        # 水先往左边流
        while V:
            curr = K
            while curr-1>=0 and heights[curr] >= heights[curr-1]:
                curr -= 1
            while curr+1 <len(heights) and heights[curr] >= heights[curr+1]:
                curr += 1
            while (curr > K) and heights[curr] >= heights[curr-1]:
                curr -= 1
            heights[curr] += 1
            V-= 1
        return heights
                
            
往左边， 往右边，直接填K
class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        
        while V:
            # loop left
            # 0~k-1
            ok = False
            index = -1
            for i in reversed(range(0, K)):
                if heights[i] > heights[i+1]: break
                if heights[i] < heights[i+1]:
                    ok = True
                    index = i
            if ok:
                heights[index] += 1
                V-= 1
                continue
       
            for i in range(K+1, len(heights)):
                if heights[i] > heights[i-1]: break
                if heights[i] < heights[i-1]:
                    ok = True
                    index = i
            if ok:
                heights[index] += 1
            else:
                heights[K] += 1
            V-= 1
        return heights

                
            