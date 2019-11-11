class Solution(object):

    def removeSameCh(self, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # aabbbbdddes -> aabbddes
        #s.translate(None, 'M')
        cur = s[0]
        count = 1
        for ch in s[1:]:
          if ch == cur:
            count += 1
            if count > 2:
              s.translate(None, ch)
          else:
            cur = ch
            count = 1
        return s


    def find(self, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # abcABC -> a?

        lowArr = [None for _ in range(32)]
        ret = None
        for ch in s:
            idx = abs(ord(ch)-ord('A'))%32
            if not lowArr[idx]:  # 存第一个a
                    lowArr[idx] = ch 
            elif abs(ord(ch)-ord(lowArr[idx])) == 32:
                if not ret:
                    ret = ch.lower()
                elif ret and ch.lower > ret:
                    ret = ch
        return ret


    def substitute(self, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        #a?b?c   abc
        # acbac
        s="?a?b?c?" 
        arrTool = "abc"
        s = '1' + s + '1'
        for i in range(len(s)):
            if s[i] == '?':
                for ch in arrTool:
                    if s[i-1] != ch and s[i+1] != ch:
                        s = s[:i] + ch + s[i+1:]
                        break
        print s[1:-2]


 Numbers With Equal Digit Sum
    def find_digit_sum(self, num):
      val = 0 
      while num:
        val += num % 10 
        num //= 10 
      return val 

    def num_digit_equal_sum(self, arr):
      digit_sum_map = {} # digit_sum: num in array
      max_val = -1 
      for num in arr:
        #[51,71,17,42]
        digit_sum = self.find_digit_sum(num) # 6,8,8,6
        if digit_sum in digit_sum_map: #42
          other_val = digit_sum_map[digit_sum] #other_val = 51
          max_val = max(max_val, other_val + num) #51+42
          digit_sum_map[digit_sum] = max(other_val, num) #update map
        else: #6:51
          digit_sum_map[digit_sum] = num

      return max_val 

Min Moves to Obtain String Without 3 Identical Consecutive Letters
  from itertools import groupby
  def minMove(S):
    return sum(len(list(g)) // 3 for _, g in groupby(S))

    S = 'baaaaa'
    print(minMove(S))

    S = 'baaabbaabbba'
    print(minMove(S))

    S = 'baabab'
    print(minMove(S))

  def minMove(S):
    moves = 0
    i,n, sum = 0,len(S), 0
    while i < n:
      ch = s[i]
      k = 0
      while s[i] == ch:
        k += 1
        i += 1
      if k/3 != 0:
        sum += k/3
    return sum
////////////////////////////////
    aCount, bCount, moves = 0, 0, 0
    for i in range(len(S)):
      if S[i] == 'a':
        aCount += 1
        bCount = 0
      else:
        bCount += 1
        aCount = 0
      if aCount == 3 or bCount == 3:
        moves += 1
        aCount = 0
        bCount = 0
    return moves

Max Network Rank
Min Swaps to Make Palindrome

from collections import Counter, defaultdict
def minSwapPalindrome(S):
    # check if can swap to palindrome
    n, cnt = len(S), Counter(S)
    odd = sum(1 for k, v in cnt.items() if v % 2)
    if odd - n % 2 > 0: return -1
    # partition into left + middle (empty if n even) + right
    aux = defaultdict(list)
    for i, c in enumerate(S):
        aux[c].append(i)
    L2R, R2L, half = [], [], (n - 1) / 2
    for c, index in aux.items():
        h = cnt[c] // 2
        # for each number
        # the first h occurence must be at left
        # the last h occurence must be at right
        L2R += [i for i in index[:h]  if i > half]
        R2L += [i for i in index[cnt[c] - h:] if i < half]
    # swap to make left and right anagram
    arr, size, move = list(S), n // 2, 0
    if n % 2 == 1:
        # if n odd, find the middle letter
        mid = [k for k, v in cnt.items() if v % 2][0]
        # find the index of its middle occurence
        mid_idx = aux[mid][cnt[mid] // 2]
        # if it is not at center, move it to center
        if mid_idx != size:
            move += abs(size - mid_idx)
            arr = arr[:mid_idx] + arr[mid_idx + 1:]
            arr.insert(size, mid)
            if len(L2R) < len(R2L):
                L2R = [i + (i > mid_idx) for i in L2R]
                L2R.append(mid_idx)
            else:
                R2L = [i - (i > mid_idx) for i in R2L]
                R2L.append(mid_idx)
    # swap the rest to make the array partitioned
    for i, j in zip(L2R, R2L):
        move += i - j
        arr[i], arr[j] = arr[j], arr[i]
    # s1 = left[::-1], s2 = right
    # find min swap to make s1 == s2
    s1, s2 = arr[:size][::-1], arr[-size:]
    i, swap = 0, 0
    while i < size: 
        j = i
        while j < size and s1[j] != s2[i]: j += 1
        if i < j < size:
            s1[i:j + 1] = [s1[j], *s1[i: j]]
            swap += j - i
        i += 1
    return move + swap
/////////////////////////
def minSwapPalindrome1(S):
    # check if can swap to palindrome
    n, cnt = len(S), Counter(S)
    odd = sum(1 for k, v in cnt.items() if v % 2)
    if odd - n % 2 > 0: return -1
    A, ans = list(S), 0
    for i in range(n // 2):
        found = False
        for j in range(i + 1, n - i)[::-1]:
            if A[i] != A[j]: continue
            found = True
            for k in range(j, n - i - 1):
                A[k], A[k + 1] = A[k + 1], A[k]
                ans += 1
            break
        if not found and n % 2 == 1:
            for k in range(i, n // 2):
                A[k], A[k + 1] = A[k + 1], A[k]
                ans += 1
    return ans

S = 'mamad'
print(minSwapPalindrome(S))

S = 'asflkj'
print(minSwapPalindrome(S))

S = 'aabb'
print(minSwapPalindrome(S))

S = 'ntiin'
print(minSwapPalindrome(S))

S = 'frrfrra'
print(minSwapPalindrome(S))


Longest Substring Without 2 Contiguous Occurrences of Letter
from itertools import groupby
def longestSubstring(s):
    result = []

    for _, chars in groupby(s):
        sublist = list(chars)

        if len(sublist)>2:
            result += sublist[:2]
            break
        else:
            result += sublist

    return ''.join(result)

S = "aabbaaaaabb"
print(longestWithout3(S))

S = "aabbaabbaabbaa"
print(longestWithout3(S))


Lexicographically Smallest String
def lexicoSmallestString(S):
    stack, deleted = [], False
    for c in S:
        while not deleted and stack and stack[-1] > c: #last element bigger than cuurent char
            stack.pop()
            deleted = True
        stack.append(c)
    ans = ''.join(stack)
    return ans if deleted else ans[:-1]

S = 'abczd'
print(lexicoSmallestString(S))

S = 'abcde'
print(lexicoSmallestString(S))

Min Deletions to Make Frequency of Each Letter Unique
from collections import Counter
def minDeleteToUniqueFreq(S): #aabbbcc
    # repeat_cnt: key:char repeat times, val: number of same repeat times char
    # repeat_cnt = Counter(Counter(S).values()) # Counter({2: 2, 3: 1})
    # ret, temp = 0, max(repeat_cnt)#ans = 0, temp = 3
    # for times, val in sorted(repeat_cnt.items(), key = lambda x: -x[1]): #order by count, decending 
    #     ret += times * val
    #     temp = min(temp, times)
    #     while val > 0 and temp > 0:
    #         ret -= temp
    #         val, temp = val - 1, temp - 1
    # return ret

def solution(str):
    l = list(str)
    l.sort()
    s = set()
    rem = 0
    if len(l) <= 1:
        return 0
    else:
        i = 0
        while i<len(l):
            count = 1
            while i+1<len(l) and l[i] == l[i + 1]:
                count += 1
                i+=1
            i+=1
            if count not in s:
                s.add(count)
            else:
                while count in s and count > 0 :
                    rem+=1
                    count-=1
                s.add(count)
        return rem
# S = 'aaaabbbbccccdddeeeffggh'
# print(minDeleteToUniqueFreq(S))

Min Deletions To Obtain String in Right Format

Notice we can partition the original string in half, deleting all B's in the left-side and all A's on the right side. 
Therefore, the trick is to find a constant time computation of the number of Bs in the left partition, 
and number of As in the right partition. Then we can iterate through all n + 1 partitions, sum the B's and A's, 
and track the minimum deletions.

For example take the string BAABAB, the partitions are as follows:

| BAABAB -> BBB
B | AABAB -> BB
BA | ABAB -> ABB
BAA | BAB -> AABB
BAAB | AB -> AAB
BAABA | B -> AAAB
BAABAB | -> AAA

Define f(i) = number of Bs up-to index i [exclusive]+ number As after index i [inclusive]
This function is the number of deletion required to transform the string to A...AB...B where index i corresponds to 
the partition before the first B.

import collections

class Solution:
    def solution(self, s):
        right = collections.Counter(s)
        left = collections.Counter()
        ans = left['B'] + right['A']
        for c in s:
            left[c] += 1
            right[c] -= 1
            ans = min(ans, left['B'] + right['A'])
        return ans

s = Solution()
assert s.solution("BAAABAB") == 2
assert s.solution("BBABAA") == 3
assert s.solution("B") == 0
assert s.solution("BAAABBBB") == 1
assert s.solution("BBBBABBB") == 1
assert s.solution("AAAAA") == 0

Unique Integers That Sum Up To 0
start with 0 if an odd number,
then just concat [i, i*-1] n/2 times.

n = 2 -> [1,-1]
n = 3 -> [0, 1, -1]
n = 4 -> [1, -1, 2, -2] etc...


def sum_to_zero(n):
    if n % 2 == 0:
        res = []
    else:
        res = [0]
        n -= 1
    for i in range(int(n/2) + 1):
        if i > 0:
            res.append(i)
            res.append(i * -1)
          
    return res


Largest Integer
Sorting + Two Pointers O(nlogn)
Array: [3,2,-2,5,-3]
After Sorting:[-3,-2,2,3,5]
Keep two pointers on the 0th and the last position respectively,
while(left<right) // To avoid zeros case
1)if the absolute values match, return the value
2) right--, if right's absolute value is greater than left's value
3)left++, if left's absolute value is greater than right's value

Extra Space O(n)
Use an Array/HashMap to keep the occurences of the element, save the absolute value in the array/hashmap. whenever you already have your absolute value in the map, compare it with the ans variable and take the maximum out of the two.
def largestint(arr):
    map = set()
    largest = 0
    for num in arr:
        if -1 * num in map:
            pos = num if num > 0 else num * -1
            if pos > largest:
                largest = pos
        else:
            map.add(num)
    return largest
def largestint(arr):
    map = set()
    largest = 0
    for num in arr:
        if -1 * num in map:
            pos = num if num > 0 else num * -1
            if pos > largest:
                largest = pos
        else:
            map.add(num)
    return largest

String Without 3 Identical Consecutive Letters
from itertools import groupby
def stringWithout3Identical(S):
    ans = ''
    for c, g in groupby(S):
        L = len(list(g))
        ans += c * min(L, 2)
    return ans
    
S = 'eedaaad'
print(stringWithout3Identical(S))

S = 'xxxtxxx'
print(stringWithout3Identical(S))

S = 'uuuuxaaaaxuuu'
print(stringWithout3Identical(S))

Longest Semi-Alternating Substring
from itertools import groupby
def longestAlternating(S):
    temp, ans = 0, 0
    for c, g in groupby(S):
        L = len(list(g))
        ans = max(ans, temp + min(L, 2))
        temp = temp + L if L < 3 else 2
    return ans
    
S = 'baaabbabbb'
print(longestAlternating(S))

S = 'babba'
print(longestAlternating(S))

S = 'abaaaa'
print(longestAlternating(S))


Min Steps to Make Piles Equal Height
from collections import Counter
def minStepEqualPiles(A):
    cnt = Counter(A)
    nums = sorted(cnt.keys(), reverse=True)
    k, ans = 0, 0
    for x in nums[:-1]:
        k += cnt[x]
        ans += k
    return ans

A = [5, 2, 1]
print(minStepEqualPiles(A))

A = [4, 5, 5, 4, 2]
print(minStepEqualPiles(A))

Day of Week
def dayOfWeek(S, K):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[(days.index(S) + K) % 7]

S, K = 'Saturday', 23
print(dayOfWeek(S, K))

 Max Possible Value
def maxPossibleValue(N):
    s = str(N)
    if N >= 0:
        i = 0
        for d in s:
            if d >= '5':
                i += 1
            else:
                break
        ans = int(s[:i] + '5' + s[i:])
    else:
        i, s = 0, s[1:]
        for d in s:
            if d <= '5':
                i += 1
            else:
                break
        ans = -int(s[:i] + '5' + s[i:])
    return ans
            

N = 268
print(maxPossibleValue(N))

N = 670
print(maxPossibleValue(N))

N = 0
print(maxPossibleValue(N))

N = -999
print(maxPossibleValue(N))

Max Inserts to Obtain String Without 3 Consecutive 'a'
from itertools import groupby
def maxInserts(S):
    ans, last = 0, '#'
    for c, g in groupby(S):
        L = len(list(g))
        if c == 'a':
            if L < 3:
                ans += 2 - L
            else:
                return -1
        else:
            ans += 2 * (L - (last == 'a'))
        last = c
    ans += 2 * (S[-1] != 'a')
    return ans
            

S = 'aabab'
print(maxInserts(S))

S = 'dog'
print(maxInserts(S))

S = 'aa'
print(maxInserts(S))

S = 'baaaa'
print(maxInserts(S))


Jump Game
def jumpGame(self, nums, ):
    nums = [3,4,2,3,10,3,1,2,1]
    mp = {}
    print self.dfs(nums, 0, mp)

    def dfs(self, nums, idx, mp): # if can jump
        if nums[idx] == 0:
            return True
        if idx in mp:
            return mp[idx]
        mp[idx] = False
        if idx-nums[idx]>0:
            if(self.dfs(nums, idx-nums[idx], mp)):
                return True
        if idx + nums[idx] < len(nums):
            if self.dfs(nums, idx+nums[idx], mp):
                return True
        return False    



Max Network Rank
from collections import Counter
def maxNetworkRank(A, B):
    deg = Counter(A + B)
    return max(deg[a] + deg[b] for a, b in zip(A, B))

A = [1, 2, 3, 4]
B = [2, 3, 1, 4]
print(maxNetworkRank(A, B))



2
    给你一个sorted array， 和一个integer n表示numbers of buckets，
   写一个function把这个sorted array 分解成n个sub array，
   使得每个sub array 的总和（weights） 差不多相同。 （approximately equals）
EX: [1,2,3,4,5], result = [[5], [4,1],[3,2]]    有点像咬零药药，不过做法肯定不一样。

因为对这个approximately equals拿不准。新建一个class，里面两个property, sum 和 list<int>。基于这个class建立一个priority queue，
排序的顺序就是sum的大小。从大到小遍历那个数组，如果pq.Count() < n就根据当前数字新建一个class加进去，否则就把当前数字加到pq的最小的里面。
我不知道该怎么证明，但自己试了几个test case，好像都对...
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sums = [0]*k
        subsum = sum(nums) / k
        nums.sort(reverse=True)
        l = len(nums)
        
        def walk(i):
            if i == l:
                return len(set(sums)) == 1
            for j in xrange(k):
                sums[j] += nums[i]
                if sums[j] <= subsum and walk(i+1):
                    return True
                sums[j] -= nums[i]
                if sums[j] == 0:
                    break
            return False        
        
        return walk(0)



4.给定两个整数A和B，求A在B里的第一个occurrence。如A = 13， B = 51367，答案就是1






"""
To invert the bits of a number, requires:
1) get the bits of the number
2) invert the numer:
    to efficiently invert bits is to use XOR with a all 1 bits number
Time complexity:O(lgn)
Space complexity:O(1)
"""
import math

def invertBits(n):
    # calculate number of bits in the given number
    x = int(math.log(n,2))
    # generate a number with x bits and all bits set, which is 1111...(x times)
    m = 1 << x
    m = m | m-1
    # calculate the bit-wise XOR of M with n
    n = n ^ m
    return n



"""
Use topology sort
1) iterate the dependecy relationships to construct a map with childrens as its values
2) use a queue to store nodes with no parents dependecy
time: O(n)
space: O(n)
"""
import defaultdict from collections
import deque

def sort(tasks, depends):
    # dependecy map: task: its dependency
    relationMap = defaultdict(set)
    # dependency count map:  taks: dependecy count
    dependencyCount = defaultdict(int)

    for depend in depends:
        parts = depend.split('<-')
        dependencies = parts[1].split(',')
        
        for denpendency in denpendencies:
            relationMap[dependency].add(parts[0])
            if denpendency not in dependencyCount:
                dependencyCount[denpendency] = 0
        dependencyCount[parts[0]] += len(dependencies)
    
    q = deque()
    for k in dependencyCount.keys():
        if dependencyCount[k] == 0:
            q.append(k)

    res = [_ for _ in len(tasks)]
    i = 0
    while q:
        cur = q.popleft()
        res[i] = curr
        if cur in relationMap:
            connections = relationMap[cur]
            for connect in connections:
                dependencyCount[connect] -= 1
                if dependencyCount[connect] == 0:
                    q.append(connect)
        i += 1
   
    return res



"""
to get approximately equal weights of n buckets:
1) get a most possible number for all subsets to reach, ex. use average: (all number sum)/n
2) go through the array to find all the possible sets
Time:O(nlogn)  because of the sort
Space: O(k) k : n buckets
"""
def groupArray(self, nums, n):
    sums = [0 for _ in range(n)]
    subsum = sum(nums)/n
    nums.sort(reverse == True)
    l = len(nums)
    
    def canGroup(i):
        if i == 1:
            return len(set(sums)) == 1
        for j in xrange(n):
            sums[j] += nums[i]
            if sums[j] <= subsum and canGroup(i+1):
                return True
            sums[j] -= nums[i]
            if sums[j] == 0:
                break
        return False
    
    return self.canGroup(0)
    






















