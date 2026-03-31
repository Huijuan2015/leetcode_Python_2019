class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        p_to_w = {}
        w_to_p = {}
        for char, word in zip(pattern, words):
            # 比如模式 abba 和字符串 dog dog dog dog。
            # 如果只查 a -> dog 和 b -> dog，你会发现它们都指向 dog
            if char in p_to_w and p_to_w[char] != word:
                return False
            if word in w_to_p and w_to_p[word] != char:
                return False
            p_to_w[char] = word
            w_to_p[word] = char
        return True
