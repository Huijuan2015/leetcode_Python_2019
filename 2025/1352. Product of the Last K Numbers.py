class ProductOfNumbers(object):

    def __init__(self):
        self.prefix = [1]
        # self.last_zero = -1

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.prefix = [1] # 清空所有乘积，重新开始
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.prefix):
            return 0 # 如果包含了 0 之后的数据，则乘积为 0
        return self.prefix[-1]//self.prefix[-1-k]

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)