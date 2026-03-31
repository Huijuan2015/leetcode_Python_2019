class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            anagrams_map[key].append(s)
        # res = []
        # for k, v in anagrams_map.items():
        #     res.append(v)
        # return res
        return list(anagrams_map.values())
