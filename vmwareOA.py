LeetCode 829 Consecutive Numbers Sum

class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        import math
        count = 1
        end = int(math.sqrt(2*N)) + 1
        for k in range(2, end):
            if (N-((k*(k-1)/2))) % k == 0:
                count += 1
        return count
        


class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        ret = []
        count = 0
        index =  1
        length = N.bit_length()
        while N:
            if N & 1:
                count += 1
                ret.insert(0,length - index + 1) # O(N)
            index += 1
            N >>= 1
        ret.insert(0, count)
        print ret

        //////////
        N_bin = bin(N)
        ret = []
        count = 0
        s = N_bin.decode()
        print s
        for i in range(2, len(s)):
            if s[i] == '1':
                ret.append(i-1)
                count += 1

        ret.insert(0, count)

        print ret


Emma and the square Numbers
class Solution(object):
    def squareNum():
        arr = ["3 9", "17 24"]
        ret = []
        #for arr
        count = 0
        tempArr = map(int, arr[0].split(' ')) #[3,9]
        # tempArr = [int(i) for i in arr[0].split(' ')]
        # print arr[0].split(' '), tempArr
        for i in range(tempArr[1]/2):
            print i
            if i*i >= tempArr[0] and i*i <= tempArr[1]:
                count += 1
        ret.append(count)
        print ret
        
           

cut the sticks
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from collections import Counter
        arr = [1,1,2,3]
        # sort(arr)
        mp = collections.Counter(arr)
        n = len(arr)
        ret = [n]
        
        for v in mp:
            n -= mp[v]
            if n > 0:
                ret.append(n)
        print ret



给一个分数，分子/分母，约分到不能再约分位置。 比如8/10，返回 4/5. 输入是List<String>,输出也是。
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        arr = ["10","20"]
        tempArr = map(int, arr)
        num1, num2 = tempArr[0], tempArr[1]
        if num2==0:
            print '分母不能为0，重新输入！'
        elif num1%num2==0:
            print num1/num2
        else:
            temp=min(num1, num2)
            for i in range(1,temp):
                if num1%i==0 and num2%i==0:
                    num1/=i 
                    num2/=i 
            print str(num1)+'/'+str(num2)
        print num1, num2

https://www.geeksforgeeks.org/minimum-incrementdecrement-to-make-array-non-increasing/


 给个array, 每次从index start， 到index end，各元素加一个数字。返回和。 
 这个题最简单，然而要求自己写std in，并且有exception处理要写一个，其实也不难。就是std in真的没写过，恶心。。
import sys

for line in sys.stdin:
    print(line)

    name = raw_input("Enter your name: ") 




