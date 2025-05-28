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


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 一门课需要上多少门前置{course：n}
        # 一门课是多少门课的前置 {c1: c2, c3, c4}
        course_n_mp = collections.defaultdict(int)
        parent_mp = collections.defaultdict(list)
        q = collections.deque()
        for c1, c2 in prerequisites: #c1 course c2 pre/parent
            course_n_mp[c1] += 1
            parent_mp[c2].append(c1)
        for c in range(numCourses): # n courses
            if course_n_mp[c] == 0: #判断是否无前置课程
                q.append(c)
        res = 0
        while q:
            c_pre = q.popleft()
            res += 1
            for c in parent_mp[c_pre]:
                course_n_mp[c] -= 1
                if course_n_mp[c] == 0:
                    q.append(c)
        return res == numCourses





