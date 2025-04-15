class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # For a given binary number, multiplying by 2 is the same as adding a zero at the end (just as we just add a zero when multiplying by ten in base 10).
        # 由于乘以 2 只是在末尾添加一个 0，所以一个数和它的两倍拥有相同数量的 1。同样地，将一个数乘以 2 并加 1（即变为奇数），其 1 的数量将比原来多 1。
        # countBits(N) = countBits(2N)
        # countBits(N) + 1 = countBits(2N + 1)
        counter = [0]
        for i in range(1, n+1):
            # counter[i] = counter[i // 2] + i % 2 整除
            counter.append(counter[i>>1] + i%2)
        return counter