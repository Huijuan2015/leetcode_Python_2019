class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        currLineLength = 0
        lines = 0
        for ch in s:
            width = widths[ord(ch)-ord('a')]
            currLineLength += width
            if currLineLength > 100:
                currLineLength = width
                lines += 1
                
        return[lines+1, currLineLength]