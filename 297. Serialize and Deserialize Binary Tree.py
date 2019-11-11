# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = ""
        self.preOrder(root)
        return self.res[:-1]
    
    def preOrder(self, root):
        if not root:
            self.res+='#,'
            return
        self.res+=(str(root.val) + ',')
        self.preOrder(root.left)
        self.preOrder(root.right)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # queue
        from collections import deque
        self.queue = deque(data.split(","))
        print self.queue
        root = self.dfs(self.queue)
        return root
    
    def dfs(self, queue): # 返回node
        if not queue:
            return
        curr = self.queue.popleft()
        if curr == '#':
            return
        node = TreeNode(curr)
        node.left = self.dfs(self.queue)
        node.right = self.dfs(self.queue)
        return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))