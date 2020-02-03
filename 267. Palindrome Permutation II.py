class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) == 1:
            return list(s)
        cnt = collections.Counter(s)
        odd = ""
        oddCnt = 0
        arr = []
        for ch, c in cnt.items():
            if c%2 != 0:
                odd = ch
                oddCnt+=1
            if oddCnt > 1:
                return []
            c /= 2
            while c:
                arr.append(ch)
                c -= 1
        # 用map中剩余的字符组成一半字符串
        visited = set()
        self.res = []
        self.findHalf(sorted(arr), odd, "", len(s)/2, visited)
        return self.res
    
    def findHalf(self, arr, odd, path, l, visited):
        if len(path) == l:
            # rightHalf = path[::-1]
            # path += odd
            self.res.append(path+odd+path[::-1])
            return
                    
        for i in range(len(arr)):
            if i-1 >= 0 and arr[i] == arr[i-1] and i-1 not in visited:
                continue
            if i not in visited:
                visited.add(i)
                self.findHalf(arr, odd, path+arr[i], l, visited)
                visited.remove(i)
            
                      
                      
        
        