"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr = head
        while curr:
            if curr.child:
                next = curr.next #store next part
                last = curr.child # store child head
                while last.next:
                    last = last.next
                curr.next = curr.child
                last.next = next
                if next: # 注意这个
                    next.prev = last
                curr.child.prev = curr
                curr.child = None
            curr = curr.next
        return head
    
    
#         if not head:
#             return head
#         self.travel(head)
#         return head
        
#     def travel(self, head):
#         # if not node:
#         #     return
#         # curr = node
       
#         if head.child: 
#             child = self.travel(head.child)
#             child.next = head.next
#             if head.next:
#                 head.next.prev = child
#             head.next = head.child
#             head.child.prev = head
#             head.child = None
#             head = child
#         if not head.next:
#             return head
#         else:
#             return self.travel(head.next)
        
        