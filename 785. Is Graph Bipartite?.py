class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        # (node, 1/-1)
        
        colors = {i:-1 for i in range(len(graph))} # node: -1表示未visit过， 要染成0/1
        for i in range(len(graph)):
            if colors[i] == -1 and not self.isValid(graph, colors, 0 , i): #0?
                return False
        return True
     #dfs          
    def isValid(self, graph, colors, color, node):#with node, if color works
        if colors[node] != -1: #被染过色
            return colors[node] == color # 
        colors[node] = color #染色
        for n in graph[node]:
            if not self.isValid(graph, colors, 1-color, n):
                return False
        return True
        
        
                    