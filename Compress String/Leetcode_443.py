class Solution:
    def compress(self, chars: List[str]) -> int:
        N = len(chars)
        read, write = 0, 0
        while read < N:
            chars[write] = chars[read]
            count = 0
            while read < N and chars[read]==chars[write]:
                read += 1
                count += 1
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] =c
                    write += 1
        
        return write