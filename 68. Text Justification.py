class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        #<= maxWidth: left-justified
        # for words; res
            # maintain a temp string list temp = []
            # maintain a current length currLen sum
            # check currLen + len(temp)+len(word) < maxWidth ? push to temp: modify temp and push to res
                # modify temp:
                # if words + (num of words-1) <= maxWidth//2: left justify lefJust(temp, currLen, maxWidth)
                # else normal justify 
                #最后一行的特殊处理
        #
        
        def leftJust(words, currLen, maxWidth): #string: understand well
            res = " ".join(words) + " " * (maxWidth - currLen -len(words) + 1)
        
        def midJust(words, currLen, maxWidth):
            # 除得尽 除不尽
            blanks = (maxWidth - currLen)//
            
        res = []
        for i in range(len(words)):

////////////            
class Solution(object):
    def fullJustify(self, words, maxWidth):
        '''
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        '''
        n = len(words)
        L = maxWidth
        i = 0     # the index of the current word   
        ans = [] 
        
        def getKwords(i):
            k = 0 # figure out how many words can fit into a line
            l = ' '.join(words[i:i+k]) 
            while len(l) <= L and i+k <= n:
                k += 1
                l = ' '.join(words[i:i+k])
            k -= 1 
            return k
        
        
        def insertSpace(i, k):
            ''' concatenate words[i:i+k] into one line'''
            l = ' '.join(words[i:i+k])       
            if k == 1 or i + k == n:        # if the line contains only one word or it is the last line  
                spaces = L - len(l)         # we just need to left assigned it
                line = l + ' ' * spaces 
            else:                           
                spaces = L - len(l) + (k-1) # total number of spaces we need insert  
                space = spaces // (k-1)     # average number of spaces we should insert between two words
                left = spaces % (k-1)       # number of 'left' words, i.e. words that have 1 more space than the other words on the right side
                if left > 0:
                    line = ( " " * (space + 1) ).join(words[i:i+left])  # left words
                    line += " " * (space + 1)                           # spaces between left words & right words
                    line += (" " * space).join(words[i+left:i+k])       # right woreds
                else: 
                    line = (" " * space).join(words[i:i+k])
            return line
        

        while i < n: 
            k = getKwords(i)  
            line = insertSpace(i, k) # create a line which contains words from words[i] to words[i+k-1]
            ans.append(line) 
            i += k 
        return ans    