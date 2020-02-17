"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root:
            head, tail = self.helper(root)
            return head
        return None
    
    def helper(self, root):
        """Idea: Construct a DLL for each subtree, then return the head and tail"""
        head, tail = root, root
        if root.left:
            lh, lt = self.helper(root.left)
            lt.right = root
            root.left = lt
            head = lh
        if root.right:
            rh, rt = self.helper(root.right)
            root.right = rh
            rh.left = root
            tail = rt
        head.left = tail
        tail.right = head
        return (head, tail)



要用定义的node, right-> next, left: prev
inorder
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
      
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return
        dummy = Node(0)
        prev = dummy
        stk = []
        node = root
        while stk or node:
            while node:
                stk.append(node)
                node = node.left
            node = stk.pop()
            node.left = prev
            prev.right = node
            prev = node
            node = node.right
        dummy.right.left = prev
        prev.right = dummy.right
        return dummy.right
 


//recursive. 很赞  Idea: Construct a DLL for each subtree, then return the head and tail
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root:
            head, tail = self.helper(root)
            return head
        return None

    def helper(self, root):
        """Idea: Construct a DLL for each subtree, then return the head and tail"""
        head, tail = root, root
        if root.left:
            lh, lt = self.helper(root.left)
            lt.right = root
            root.left = lt
            head = lh
        if root.right:
            rh, rt = self.helper(root.right)
            rh.left = root
            root.right = rh
            tail = rt
        head.left = tail
        tail.right = head
        return (head, tail)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        ht = self.helper(root)
        return ht[0]
    
    # return [min, max]
    def helper(self, root):
        if not root:
            return [None,None]
        left = self.helper(root.left) #[min, max]
        right = self.helper(root.right)
        ret = [None for i in xrange(2)]
        
        if left[1]:
            left[1].right = root
            root.left = left[1]
            ret[0] = left[0]
        else:
            ret[0] = root
        if right[0]:
            root.right = right[0]
            right[0].left = root
            ret[1] = right[1]
        else:
            ret[1] = root
        
        ret[0].left = ret[1]
        ret[1].right = ret[0]
        
        return ret

//错误：自己定义了node

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class DoubleLLNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        dummy = DoubleLLNode(0)
        # currListNode = ListNode(0)
        curr = dummy
        stk = [(root, False)]
        while stk:
            treeNode, visited = stk.pop()
            if treeNode:
                print treeNode.val
                if visited:
                    curr.next = DoubleLLNode(treeNode.val)
                    curr.next.prev = curr
                    curr = curr.next
                    continue
                print treeNode
                stk.append((treeNode.right, False))
                stk.append((treeNode, True))
                stk.append((treeNode.left, False))
                
        curr.next = dummy.next
        dummy.next.prev = curr.next
        return dummy.next


        