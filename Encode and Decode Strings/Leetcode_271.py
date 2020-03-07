class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        lengths = map(str, (len(s) for s in strs))
        return '.'.join(lengths) + '#' + ''.join(s for s in strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if s == '#': return []
        i = s.index('#')
        lengths = map(int, s[:i].split('.'))
        res = []
        j = i+1
        for l in lengths:
            res += [s[j:j+l]] if l>0 else [""]
            j += l
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
