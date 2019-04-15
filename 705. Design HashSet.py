class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._data={}

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self._data:
            return
        else:
            self._data[key] = 1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self._data:
            del self._data[key]

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self._data:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)