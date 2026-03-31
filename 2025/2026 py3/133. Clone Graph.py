"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val)

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
        return visited[node]




"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = {}
        
        def dfs(original_node):
            if not original_node:
                return None
            if original_node in visited:
                return visited[original_node]
                
            clone_node = Node(original_node.val)
            visited[original_node] = clone_node
            
            for neighbor in original_node.neighbors:
                # 第一步：去“克隆工厂”问问，这个邻居有没有被克隆过？
    # 如果没克隆过，dfs 会去创建一个新的；如果克隆过了，dfs 会直接从 visited 拿给你。
                clone_neighbors = dfs(neighbor)
                clone_node.neighbors.append(clone_neighbors)

            return clone_node
        return dfs(node)
