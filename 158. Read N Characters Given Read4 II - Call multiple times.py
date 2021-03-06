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
    cache = [None for _ in range(4)] #max 4
    cacheEnd = 0
    cacheStart = 0
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        # 1byte by 1byte
        bufLoc = 0
        
        while n > 0:
            if self.cacheStart < self.cacheEnd:
                buf[bufLoc] = self.cache[self.cacheStart]
                self.cacheStart += 1
                bufLoc += 1
                n -= 1

            else:
                self.cacheEnd = read4(self.cache)
                self.cacheStart = 0
                if self.cacheEnd == 0:
                    break
        return bufLoc

            