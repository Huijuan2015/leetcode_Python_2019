there are 3 cases:

Case 1:
“AB-CDE-F-….-YZ” (‘-’ denotes a space)
reach to the space before F

Case 2:
“AB-CDE-F-…._YZ” (‘-’ denotes a space)
reach to exactly E

Case 3:
“AB-CDE-F-….-YZ” (‘-’ denotes a space)
reach to D

case 1, I can count one more bit and go to next line
case 2, I can count two more bits and go to next line
case 3, I have to move the cursor back until it reach to some space, and go to next line

When I go through all the rows, how many bits did I counted? Let’s say L, then the answer should be L / length of the string

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence) + ' '
        curr = 0
        n = len(s)
        for i in range(rows):
            curr += cols - 1
            if s[curr%n] == ' ':
                curr += 1
            elif s[(curr+1)%n] == ' ':
                curr += 2
            else:
                while curr > 0 and s[(curr-1)%n] != ' ':
                    curr -= 1
        return curr/n
            