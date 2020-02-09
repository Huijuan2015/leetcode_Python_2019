class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        colors = {i:-1 for i in range(len(graph))}
        for i in range(len(graph)):
            if colors[i] == -1 and not self.isValid(graph, colors, 0, i):
                return False
        return True
    def isValid(self, graph, colors, color, node):
        #欲染色， 先判断是否被染过
        if colors[node] != -1:
            return colors[node] == color
        colors[node] = color
        for n in graph[node]:
            # 欲给两端染成与node不同的颜色
            if not self.isValid(graph, colors, 1-color, n):
                return False
        return True


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        # (node, 1/0)
        # -1：未被染色， 需要将node及其children染成1/0间隔色
        colors = {i:-1 for i in range(len(graph))} # node: -1表示未visit过， 要染成0/1
        for i in range(len(graph)):
            #当node未被染色时，要为这个node及其children染色，并判断是否valid
            if colors[i] == -1 and not self.isValid(graph, colors, 0 , i): 
                return False
        return True
     #dfs          
    def isValid(self, graph, colors, color, node):#with node, if color works
        if colors[node] != -1: #如果被染过色，直接判断颜色是否是预期color
            return colors[node] == color # 
        colors[node] = color #如果未染色，则染成期望color再继续dfs孩子
        for n in graph[node]:
            if not self.isValid(graph, colors, 1-color, n):
                return False
        return True
        
        
                    