class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 共有 pow(k, n)个答案， 从n个0开始， 下一个答案向后移一个
        # 然后分别与k个数组合，验证是否在结果set中，不在就加入
        passwords = set()
        res = '0'*(n-1)

        for i in range(pow(k, n)):# 为什么要循环这么多次， 2个密码共享n-1位才可以保证总长度最短
            prev = res[-n+1:] if n > 1 else '' #last n-1 位， 当n=1的情况
            for j in range(k-1, -1, -1): #为什么倒序：不会出现00导致循环提前结束
                prev += str(j)
                if prev not in passwords:
                    passwords.add(prev)
                    res += str(j)
                    break
        return res            
            
        