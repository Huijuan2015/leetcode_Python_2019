class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        # mp = {ch:idx for idx, ch in enumerate(source)}
        mp = collections.defaultdict(list)
        for idx, ch in enumerate(source):
            mp[ch].append(idx)
        n = len(target)
        dp = [-1 for _ in range(n)] #dp[i] 0~i需要dp[i]个source
        if target[0] not in mp:
            return -1
        dp[0] = 1
        lastIdx = mp[target[0]][0]
        for i in range(1, n):
            if target[i] not in mp:
                return -1
            # find a smallest bigger
            curr = mp[target[i]] # 0,1,2,3,4
            j = 0
            while j < len(curr):
                if curr[j] <= lastIdx:

                    j += 1
                    continue
                else:
                    # print j
                    dp[i] = dp[i-1]
                    lastIdx = curr[j]
                    break
            # print j
            if j == len(curr):
                dp[i] = dp[i-1]+1
                lastIdx = curr[0]
        # print dp
        return dp[-1]
                            
                