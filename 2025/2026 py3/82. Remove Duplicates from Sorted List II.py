# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        lastDistinct = dummy
        while head:
            if head.next and head.val == head.next.val:
                dupVal = head.val
                while head and head.val == dupVal:
                    head = head.next
                lastDistinct.next = head
            else:
                lastDistinct = head
                head = head.next
        return dummy.next



