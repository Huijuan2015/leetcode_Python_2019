class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # numCourses   
        # prerequisites [[a1,b1], [a2, b2]...]
        # 一门课是多少门课的前置 {{a: b, c, d},..}
        # 一门课还需要上多少门前置{c: 3, a:0}
        mp = collections.defaultdict(list)
        preCnt = collections.defaultdict(int)
        for pre in prerequisites:
            course, parent = pre
            mp[parent].append(course)
            preCnt[course] += 1
        q = collections.deque()
        cnt = 0
        for i in range(numCourses):
            if i not in preCnt:
                q.append(i)
        while q:
            parent = q.popleft()
            cnt += 1 #课上完了
            for course in mp[parent]:
                preCnt[course] -= 1
                if preCnt[course] == 0:
                    q.append(course)
        return cnt == numCourses







