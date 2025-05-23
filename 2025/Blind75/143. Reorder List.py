# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 取后半段，reverse，然后与前半段插入
        if not head:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow.next
        slow.next = None
        head1 = head
        head2 = self.reverse(middle)

        while head1 and head2:
            tmp1, tmp2 = head1.next, head2.next
            head1.next = head2
            head2.next = tmp1
            head1 = tmp1
            head2 = tmp2

    def reverse(self, head):
        dummy = ListNode(0)
        curr = head
        while curr:
            tmp = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = tmp
        return dummy.next
        