class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = [0 for _ in range(26)]
        for ch in tasks:
            cnt[ord(ch)-ord('A')] += 1
        cnt.sort()
        print cnt
        i = 25
        while i>=0 and cnt[i] == cnt[25]: #出现次数最多的字母个数，是最后一行的长度？
            i-=1
        return max(len(tasks), (cnt[25]-1)*(n+1)+25-i) # 前cnt[25]-1行 + 最后一行25-i AB单个总和：25-i
        # 没有空闲时间：len(tasks)
        # 有空闲时间 idle： (cnt[25]-1)*(n+1)+25-i