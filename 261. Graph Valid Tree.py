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
                
        