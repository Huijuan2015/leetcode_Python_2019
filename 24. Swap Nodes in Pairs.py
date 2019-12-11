# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        if not head or not head.next:
            return head
        while head and head.next:
            nextHead = head.next.next
            
            curr.next = head.next
            head.next.next = head
            head.next = nextHead
            
            curr = head
            head = nextHead
            
        return dummy.next
            
            


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Recursively?
        if not head or not head.next:
            return head
        next = head.next
        behind = next.next
        next.next = head
        head.next = self.swapPairs(behind)
        #head = next
        return next
#         dummy = prev = ListNode(0)
#         dummy.next = head
#         while head and head.next:
#             # swap head and head.next
#             tmp = head.next
#             head.next = tmp.next
#             tmp.next = head
            
#             # prev connection
#             prev.next = tmp
#             head = head.next
#             prev = tmp.next
#         return dummy.next
        
       
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(0)
        curr= head
        要记住一个tail
        while curr and curr.next:
            tmp = curr.next.next
            tail.next = curr.next
            curr.next .next = curr
            curr.next = tmp
            curr = tmp
            tail = tail.next.next
        tail.next = curr #剩一个
        return dummy.next



Recursively
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        先swap前两个，然后不断递归
        if not head or not head.next:
            return head
        nextHead = head.next.next
        #head, head.next = head.next, head
        head.next.next = head
        head = head.next
        head.next.next = self.swapPairs(nextHead)
        return head