class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num == first or num == second or num == third:
                continue
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        return third if third != float('-inf') else first


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #维护一个长度为3的set
        top3 = set()
        for num in nums:
            top3.add(num)
            if len(top3) > 3:
                top3.remove(min(top3))
        return min(top3) if len(top3) == 3 else max(top3)