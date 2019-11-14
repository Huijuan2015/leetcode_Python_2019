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
        curr = levelHead = root # levelHead points to the head node of current level 
        while curr:
            levelHead = curr
            while curr:  # cur level: left.next = right, right.next = next.left
                if curr.left:  
                    curr.left.next = curr.right
                    if curr.next://???
                        curr.right.next = curr.next.left
                curr = curr.next  
            curr = levelHead.left          
        return root


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
        #记下当前层，连接当前层的下一层
        if not root:
            return
        curr = root

        while curr:
            head = curr
            while curr:
                if curr.left:
                    curr.left.next = curr.right
                if curr.next and curr.right:
                    curr.right.next = curr.next.left
                curr = curr.next
            curr = head.left
        return root
            
            