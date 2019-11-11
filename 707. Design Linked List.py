class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if not self.head:
            return -1
        curr = self.head
        while index > 0:
            index -= 1
            if not curr:
                return -1
            curr = curr.next
        return curr.val if curr else -1
        # curr = self.head
        # for i in range(index):
        #     curr = curr.next
        # return curr.val if curr else -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        curr = ListNode(val)
        curr.next = self.head
        self.head = curr


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        curr = self.head
        if not curr:
            self.head = ListNode(val)
        else:
            while curr.next :
                curr = curr.next
            curr.next = ListNode(val)


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            while index > 1:
                index -= 1
                if not curr:
                    return
                curr = curr.next
            node = ListNode(val)
            node.next = curr.next #不要忘记
            curr.next = node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        curr = self.head
        if index == 0:
            self.head = self.head.next
        while index > 1:
            index -= 1
            if not curr:
                return
            curr = curr.next
        curr.next = curr.next.next if curr.next else None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)