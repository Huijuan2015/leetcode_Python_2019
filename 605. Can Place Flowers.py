class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        for i in range(1, len(flowerbed) - 1): # 0100 2
            if not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
                n -= 1
                flowerbed[i] = 1
        return n <= 0