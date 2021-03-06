class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mp={}
        self.nums=[]

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        #number:count
        if number in self.mp:
            self.mp[number] += 1
        else:
            self.mp[number] = 1
        self.nums.append(number)
        
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i, n in enumerate(self.nums):
            find = value-n
            if (find in self.mp and find != n) or (find in self.mp and find == n and self.mp[find]>1) :
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)




class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.mp = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.data.append(number)
        length = len(self.data)
        self.mp[number] = length - 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i, num in enumerate(self.data):
            find = value - num
            if find in self.mp and self.mp[find] != i:
                return True
        return False
                


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)