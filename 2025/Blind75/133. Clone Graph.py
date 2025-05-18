DFS
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            cloneNode = Node(node.val)
            visited[node] = cloneNode

            for neighbor in node.neighbors:
                cloneNode.neighbors.append(dfs(neighbor))
            
            return cloneNode
        return dfs(node)


BFS
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        nodeClone = Node(node.val, [])
        visited = {node:nodeClone}
        queue = collections.deque([node])
        while queue:
            currNode = queue.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in visited:
                    neighborClone = Node(neighbor.val, [])
                    visited[neighbor] = neighborClone
                    visited[currNode].neighbors.append(neighborClone)
                    queue.append(neighbor)
                else:
                    visited[currNode].neighbors.append(visited[neighbor])
        return nodeClone

        

