class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        for s in strings:
            key = []
            for i in range(1, len(s)):
                # 我们用的是 差值 mod 26，它表示的是 'b' 变成 'a' 需要向前偏移 1 步，也就是等价于从 'b' 向后偏移 25 步（因为我们统一采用向后偏移的方式）。
                diff = (ord(s[i]) - ord(s[i-1])) % 26 # -1 % 26 = 25
                key.append(diff)
            groups[tuple(key)].append(s)
        return list(groups.values())