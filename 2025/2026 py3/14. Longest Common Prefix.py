class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""

        for i, ch in enumerate(strs[0]):
            for s in strs[1:]:
                if i == len(s) or s[i] != ch:
                    return strs[0][:i]
        return strs[0]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
            