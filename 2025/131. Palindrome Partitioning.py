class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def isPalindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:]) # Python 列表深拷贝
                return
            for end in range(start+1, len(s)+1):
                prefix = s[start:end]
                if isPalindrome(prefix):
                    path.append(prefix)
                    backtrack(end, path)
                    path.pop()
        backtrack(0, [])
        return res