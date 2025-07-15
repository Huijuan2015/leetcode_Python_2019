class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        # 升序排列的、内部的区间不重叠
        # 相交或不相交
        i, j = 0, 0
        result = []
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            start = max(a_start, b_start)
            end = min(a_end, b_end)
            # 查看是否有交集
            if start <= end:
                result.append([start, end])
            
            # 移动右端点较小的那一个区间的指针
            if a_end < b_end:
                i += 1
            else:
                j += 1
        return result
