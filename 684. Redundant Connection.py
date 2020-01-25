class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = [_ for _ in range(1001)]
        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])
        
        def union(x, y):
            parent[find(y)] = x
            
        for x,y in edges:
            if find(x) == find(y):
                return [x, y]
            else:
                union(x, y)
            
        
        
        