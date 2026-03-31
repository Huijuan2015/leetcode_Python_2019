class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ") 
        res = []
        for word in reversed(arr):
            if word != '':
                res.append(word)
        return " ".join(res)


# 如果用split()会 自动处理所有空格问题
# s.split()



去零，翻转整个字符串，翻转单词
class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s)
        n = len(l)

        slow, fast = 0, 0
        while fast < n:
            if l[fast] != ' ':
                if slow != 0:
                    l[slow] = ' ' #前面加一个空格， 形成新的单词
                    slow += 1
                while fast < n and l[fast] != ' ':
                    l[slow] = l[fast]
                    slow += 1
                    fast += 1
            else:
                fast += 1
            
        l = l[:slow]
        
        def reverse(arr, i , j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        reverse(l, 0, len(l)-1)

        start = 0
        for end in range(len(l) + 1):
            if end == len(l) or l[end] == ' ':
                reverse(l, start, end-1)
                start =  end + 1
        return ''.join(l)
            
