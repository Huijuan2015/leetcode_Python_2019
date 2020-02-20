class Solution(object):
    def kEmptySlots(self, bulbs, k):
        """
        :type bulbs: List[int]
        :type K: int
        :rtype: int
        """
        days = [0 for _ in range(len(bulbs))]
        for day, pos in enumerate(bulbs, 1):
            days[pos-1] = day # days[i] = t 表示在 i+1 位置上会在第t天放上花
        print days
        
        ans = float('inf')
        i, j = 0, k+1
        while j < len(bulbs):
            for b in range(i+1, j):
                if days[b] < days[i] or days[b] < days[j]:
                    i, j = b, b+k+1
                    break
            else:
                ans = min(ans, max(days[i], days[j]))
                i, j = j, j+k+1

        return ans if ans < float('inf') else -1