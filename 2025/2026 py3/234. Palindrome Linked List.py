# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        #找中点，翻转后半部分，比较
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #翻转
        prev = None
        curr = slow #偶数 1221，停在第二个2，奇数停在中间
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # prev is new head2
        # compare prev and head(till slow)
        left, right = head, prev
        while right: # 当我们反转后半部分时，前半部分的最后一个节点依然指向着 slow
            if right.val != left.val:
                return False
            else:
                right = right.next
                left = left.next
        return True