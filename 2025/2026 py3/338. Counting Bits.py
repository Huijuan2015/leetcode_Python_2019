class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(1, n+1):
            # i 的 1 的个数 = 擦掉一个 1 后的那个数的个数 + 1
            ans[i] = ans[i&(i-1)] + 1
        return ans


class Solution:
    def countBits(self, n: int) -> List[int]:
        # 利用奇偶性 (Bit Shifting)
        # 如果 i 是偶数：它的二进制最后一位是 0。右移一位（除以 2）不会改变 1 的个数。
        # 例子：6 (110) 和 3 (011) 的 1 数量相同。
        # 如果 i 是奇数：它的二进制最后一位是 1。比它除以 2 的结果多一个 1。
        # 例子：7 (111) 比 3 (011) 多一个 1。
        ans = [0] * (n+1)
        for i in range(1, n+1):
            # i >> 1 相当于 i // 2
            # i & 1 检查最后一位是不是 1
            ans[i] = ans[i>>1]+(i&1)
        return ans
