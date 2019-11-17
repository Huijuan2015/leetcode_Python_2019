class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if not letters:
            return
        # ans = ""
        # diff = float('inf')
        # 找到 letter 使得letter-target diff最小
        for l in letters:
            if l > target:
                return l
            # tmp = ord(l) - ord(target)
            # if tmp <= diff :
            #     ans = l
            #     diff = tmp
        return letters[0]
    
    二分法更快


    class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
    # 二分法更快
        # if target >= letters[-1]:
        #     return letters[0] #如果没有，那就返回第一个字母
        start = 0
        end = len(letters)-1
        ans = 0
        while start <= end:
            mid = start + (end-start)//2
            if target>=letters[mid]:
                start = mid+1
            else:
                end = mid-1
                ans = mid
        return letters[ans]
            
                
                
    