class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # build graph and bfs
        graph = collections.defaultdict(set)
        if len(edges) != n-1:
            return False
        for edge in edges:
            e1, e2 = edge
            graph[e1].add(e2)
            graph[e2].add(e1)
        if not graph:
            return True
        q = collections.deque()
        q.append(graph.keys()[0])
        visited = set()
        
        while q:
            node = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            for nbr in graph[node]:
                q.append(nbr)
                graph[nbr].remove(node)
            graph.pop(node)
        return not graph
        
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # build graph

        #
        from collections import defaultdict
        graph = defaultdict(set)
        if len(edges) != n-1:
            return False
        for edge in edges:
            i, j = edge
            graph[i].add(j)
            graph[j].add(i)
        if not graph:
            return True
        stk = []
        stk.append(graph.keys()[0])
        visited = set()
        # visited.add(stk[0])
        while stk:
            # print stk, visited
            node = stk.pop()
            if node in visited:
                return False
            visited.add(node)
            for nbr in graph[node]:
                stk.append(nbr)
                graph[nbr].remove(node)
            graph.pop(node)
        return not graph
                
        