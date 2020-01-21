class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # 前提课数量map + 后续课graph
        parents = collections.defaultdict(int)
        graph = collections.defaultdict(set)
        for prerequisite in prerequisites:
            c1, c2 = prerequisite # c2是c1的前提课
            graph[c2].add(c1) #后续课
            parents[c1] += 1
        q = collections.deque()
        path = []
        #找到出？度为0的点 不需要前提课的点
        for i in range(numCourses):
            if i not in parents:
                q.append(i)
        while q:
            curr = q.popleft()
            path.append(curr)
            for c in graph[curr]:
                parents[c] -= 1
                if parents[c] == 0:
                    q.append(c)
        return path if len(path) == numCourses else []
        
            