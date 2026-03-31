class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = [str(num) for num in nums]
        
        def compare(x, y):
            if x+y >y+x:
                return -1
            elif x+y < y+x:
                return 1
            else:
                return 0
        
        strs.sort(key = cmp_to_key(compare)) #自定义比较函数
        if strs[0] =='0':
            return '0'
        return "".join(strs)