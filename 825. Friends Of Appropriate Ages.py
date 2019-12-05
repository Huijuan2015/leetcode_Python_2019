TLE:

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        if not ages or len(ages)<2:
            return 0
        ans = 0
        ages.sort(reverse = True)
        # print ages
        for i in range(len(ages)-1): # A->i
            for j in range(i+1, len(ages)):
                # print i, j
                if self.isValid(i, j, ages):
                    ans += 1
                    if ages[i] == ages[j]:
                        ans += 1
        return ans
    
    def isValid(self, i, j, ages):
        if ages[j] <= 0.5*ages[i] + 7 or ages[j] > ages[i] or (ages[j] > 100 and ages[i] < 100):
            return False
        return True
                


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        if not ages or len(ages)<2:
            return 0
        ans = 0

        cnt = collections.Counter(ages)
        for age1, n1, in cnt.items():
            for age2, n2, in cnt.items():
                if 0.5*age1+7 < age2 and age1 >= age2:
                    ans += n1 * n2
                    if age1 == age2: #4*4=>4*3排列
                        ans -= n1
                        
        return ans

                

