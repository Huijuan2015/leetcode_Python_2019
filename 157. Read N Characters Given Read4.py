"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of charsacters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = n//4+1 if n%4 > 0 else n//4 # string 读几轮
        j = 0 #actual characters read. also the next idx of string
        
        while i > 0: # 一轮读4个
            buf4 = [None for _ in range(4)]
            cnt = read4(buf4)
            cnt = min(n-j, cnt)
            # copy:
            for ch in buf4[:cnt]:
                buf[j] = ch
                j += 1
            i -= 1
        return j
            
            