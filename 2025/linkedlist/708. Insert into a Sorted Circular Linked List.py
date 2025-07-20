"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
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
        #     •	遍历链表，找插入位置：
        # •	如果 cur.val <= insertVal <= cur.next.val：插入
        # •	如果 cur.val > cur.next.val（最大值到最小值拐点）：
        # •	如果 insertVal >= cur.val（更大）或 insertVal <= cur.next.val（更小） → 插入
        # •	如果遍历一圈还没插入（所有值一样 or insertVal 不符合任何条件），插入任意位置都可以
        new_node = Node(insertVal)

        # Case 1: 空链表
        if not head:
            new_node.next = new_node
            return new_node
        
        prev, curr = head, head.next
        inserted = False

        while True:
            # Case 2.1: insertVal 介于 prev 和 curr 之间
            if prev.val <= insertVal <= curr.val:
                inserted = True
            # Case 2.2: 在最大值和最小值之间插入（"折断点"） 
            # 比如插入5或者0 到 [3 → 4 → 1]
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val: #?
                    insertVal = True
            
            if inserted:
                prev.next = new_node
                new_node.next = curr
                return head
            
            prev, curr = curr, curr.next
            # 已经绕一圈还没插入：说明所有节点值相等 或 插入点无所谓
            if prev == head:
                break
        # Case 3: 所有节点值相等，或找不到合适点，插入任意位置
        prev.next = new_node
        new_node.next = curr
        return head


		