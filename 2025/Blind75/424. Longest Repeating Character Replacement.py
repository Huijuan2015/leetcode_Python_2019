class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # 在每个窗口中，我们允许最多 k 次替换，保留出现次数最多的那个字符，其它的字符如果不一样就替换掉。
        # 只要替换次数不超过 k，窗口就继续扩大；一旦超过 k，就缩小窗口
        max_count = 0
        left = 0
        freq = {} #

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_count =  max(max_count, freq[s[right]])

            # 窗口长度 - 出现最多字符的数量 = 需要替换的字符数量。
            if right - left + 1 - max_count > k:
                freq[s[left]] -= 1
                left += 1
        return len(s) - left


        