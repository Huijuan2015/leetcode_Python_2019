class MyHashMap:

    def __init__(self):
        self.base = 769
        self.table = [[] for _ in range(self.base)]

    def _hash(self, key:int) -> int:
        return key%self.base

# self.base = 5（我们假设只有 5 个桶，编号 0 到 4）。

# self.table 是这排储物柜
# “链地址法”。0 号桶是个列表，它能存多个东西。我们把 不唯一的KV pair 到列表末尾。
    def put(self, key: int, value: int) -> None:
        bucket = self.table[self._hash(key)]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket = self.table[self._hash(key)]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        bucket = self.table[self._hash(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)