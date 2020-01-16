class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        mp = collections.defaultdict(list)#一门课是多少门课的前提
        #依赖
        parentCnt = collections.defaultdict(int)#学一门课还需要学多少门课
        for prerequisite in prerequisites: # key:
            c1, c2 = prerequisite
            mp[c2].append(c1)
            parentCnt[c1] +=1
        q = collections.deque()    
        cnt = 0
        for i in range(numCourses):
            if not parentCnt[i]:
                q.append(i)    
        while q: #依赖为0才append进q
            course = q.popleft()
            cnt += 1
            for c in mp[course]:
                parentCnt[c] -= 1
                if parentCnt[c] == 0:
                    q.append(c)
        # print cnt
        return cnt == numCourses
                    
                