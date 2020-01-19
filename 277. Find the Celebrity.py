
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        # get the only possible candidate
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
                
        # 要查candidate是否不知道比它小的数 and 比它小的数都知道candidate
        # 要查比它大的数是否都知道candidate
        for i in range(n):
            if i < candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
            if i > candidate and not knows(i, candidate):
                return -1
        return candidate
                
            

TLE

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        know = collections.defaultdict(int)
        known = collections.defaultdict(int)
        
        for i in range(n):
            for j in range(n):
                if i != j and knows(i, j):
                    know[i] += 1
                    known[j] += 1
        res = -1
        for i in range(n):
            if know[i] == 0 and known[i] == n-1:
                res = i
        return res
        