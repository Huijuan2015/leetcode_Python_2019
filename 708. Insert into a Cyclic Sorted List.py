"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        newNode = Node(insertVal, head)
        if not head:
            return newNode

        curr = head
        # prev = Node(0,curr)
        prev, curr = head, head.next
         # 避免找pair的时候进入死循环，无论找没有找到，都只循环一次。
        while head != curr:
            if prev.val <= insertVal <= curr.val: # 1,3中间插入2
                break
            elif prev.val > curr.val and (insertVal <= curr.val or prev.val <= insertVal): # 1 4中间插入0或者5
                break
            prev = prev.next
            curr = curr.next

        prev.next = newNode
        newNode.next = curr
        return head
    
    
    
    
        # while curr.val >= insertVal:
        #     prev = curr
        #     curr = curr.next
        # next = curr.next #3
        # # print prev.val, curr.val, next.val
        # if next.val <= insertVal: #insert as biggest
        #     prev.next = newNode
        #     newNode.next = curr
        # else: #insert as smallest
        #     curr.next = newNode
        #     newNode.next = next
        #     # print prev.val, prev.next.val, prev.next.next.val
        # return head
            
        