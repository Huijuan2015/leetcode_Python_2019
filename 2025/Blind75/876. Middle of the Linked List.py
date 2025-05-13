# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = fast = head

        while slow.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast.next == None or fast.next.next == None:
                break
        return slow if not fast.next else slow.next