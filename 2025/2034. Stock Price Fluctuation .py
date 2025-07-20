class StockPrice(object):

    def __init__(self):
        self.timestamp_price = {} #{time: price}
        self.max_heap = []
        self.min_heap = []
        self.latest_time = 0

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.timestamp_price[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self):
        """
        :rtype: int
        """
        return self.timestamp_price[self.latest_time]
        

    def maximum(self):
        """
        :rtype: int
        """
        # lazy removal
        while True:
            price, ts = self.max_heap[0]
            if self.timestamp_price[ts] == -price:
                return -price
            heapq.heappop(self.max_heap)
        
    def minimum(self):
        """
        :rtype: int
        """
        while True:
            price, ts = self.min_heap[0]
            if self.timestamp_price[ts] == price:
                return price
            heapq.heappop(self.min_heap)
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()