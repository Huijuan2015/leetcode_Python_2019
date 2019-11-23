class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        if n == 1:
            self.res.append('0')
        
        self.mp = {'6':'9','8':'8', '9':'6', '1':'1', '0':'0'}
        
        self.combination(n, "")
        return self.res
        # n: n//2 *2
    def combination(self, n, path):
        if (n%2 == 0 and n//2 == len(path)) or (n%2 == 1 and n//2 +1 == len(path)):
            self.nextHalf(n, path)
            return
        for num in ['6','9','8','1','0']:
            self.combination(n, path+num)
        
    
    def nextHalf(self, n, path):
        last = ''
        print path
        if path[0] == '0':
            return
        if n%2 == 1: #奇数
            if path[-1] not in ['1', '8', '0']:
                return
            last = path[-1]
            path = path[:-1]
        for num in path[::-1]:
            last += self.mp[num]
        path = path + last
        self.res.append(path)
            

//递归
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        return self.helper(n, n)

    def helper(self, currLen, n):
        curr = []
        if currLen == 0:
            return [""]
        if currLen == 1:
            curr = ["0", "1", "8"]
            return curr
        paths = self.helper(currLen-2, n)
        for path in paths:
            if currLen != n:
                curr.append("0"+path+"0")
            curr.append("1"+path+"1")
            curr.append("6"+path+"9")
            curr.append("8"+path+"8")
            curr.append("9"+path+"6")  
        return curr
        
        
            