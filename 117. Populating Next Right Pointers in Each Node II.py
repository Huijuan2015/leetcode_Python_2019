"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        currLevel = [root]
        
        while currLevel: # 1 level
            nextLevel = []
            for i in xrange(len(currLevel)):
                if i < len(currLevel) - 1:
                    currLevel[i].next = currLevel[i+1]
                if currLevel[i].left:
                    nextLevel.append(currLevel[i].left)
                if currLevel[i].right:
                    nextLevel.append(currLevel[i].right) 
            currLevel = nextLevel
        return root
///
The algorithm is a BFS or level order traversal. We go through the tree level by level. node is the pointer in the parent level, tail is the tail pointer in the child level.
The parent level can be view as a singly linked list or queue, which we can traversal easily with a pointer.
Connect the tail with every one of the possible nodes in child level, update it only if the connected node is not nil.
Do this one level by one level. The whole thing is quite straightforward.

Python

def connect(self, node):
    tail = dummy = TreeLinkNode(0)
    while node:
        tail.next = node.left
        if tail.next:
            tail = tail.next
        tail.next = node.right
        if tail.next:
            tail = tail.next
        node = node.next
        if not node:
            tail = dummy
            node = dummy.next            

                        
                        