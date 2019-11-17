# top 10%
class Solution:
    
    def __init__(self):
        self.bp = 0
        self.read_chars = 0
        self.buffer = ['']*4
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        tot_chars = 0
        while tot_chars < n:
            if self.bp == self.read_chars:
                self.bp = 0
                self.read_chars = read4(self.buffer)
                if self.read_chars == 0:
                    break
            buf[tot_chars] = self.buffer[self.bp]
            tot_chars += 1
            self.bp += 1
        return tot_chars