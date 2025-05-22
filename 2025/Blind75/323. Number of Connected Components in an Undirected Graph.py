    遍历所有节点：
    •   如果没访问过，用 DFS 从该节点出发，标记一整块连通区域
    •   每次新的 DFS 表示发现一个新的连通分量

    class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False]*n
        
        def dfs(i):
            visited[i] = True
            for neighbor in graph[i]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count
                
        
        
        

