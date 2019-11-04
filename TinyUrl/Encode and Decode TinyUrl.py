# LC 535

import random

class Codec:
    
    alphabet = string.ascii_letters + '0123456789'
    
    def __init__(self):
        self.long2short = {}
        self.short2long = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.long2short:
            shortUrl = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if shortUrl not in self.short2long:
                self.short2long[shortUrl] = longUrl
                self.long2short[longUrl] = shortUrl
        return "http://tinyurl.com/" + self.long2short[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.short2long[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
