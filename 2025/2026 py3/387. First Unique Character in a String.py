class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = collections.Counter(s)
        for i, ch in enumerate(s):
            if mp[ch] == 1:
                return i
        return -1



class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        res = float('inf')
        
        # 遍历 26 个字母，而不是遍历千万个字符
        for char, freq in count.items():
            if freq == 1:
                # 找到该唯一字符在原字符串中的索引
                res = min(res, s.find(char))
        
        return res if res != float('inf') else -1