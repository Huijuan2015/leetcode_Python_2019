class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # valid tree: no circle
        if len(edges) != n-1:
            return False
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                # •	如果是父节点跳过（避免回头）。
                if neighbor == parent:
                    continue
                # •	如果相邻节点已经访问过，说明有环，返回 False。
                # •	否则递归访问相邻节点。
                if neighbor in visited or not dfs(neighbor, node):
                    return False
            return True
        # 遍历结束后，如果访问的节点数量等于 n，说明连通
        return dfs(0, -1) and len(visited) == n


#union find?