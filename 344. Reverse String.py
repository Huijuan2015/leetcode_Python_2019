class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # not working
        # mid = len(s)/2
        # if mid == 0:
        #     return s
        # left = self.reverseString(s[:mid])
        # right = self.reverseString(s[mid:])
        # s = right+left
        
        start, end = 0, len(s)-1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s
        
        def helper(start, end, ls):
            if start >= end:
                return
        
            # swap the first and last element
            ls[start], ls[end] = ls[end], ls[start]        

            return helper(start+1, end-1, ls)
    
        helper(0, len(s)-1, s)