class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        i, fldr = 0, ''
        while i<len(folder):
            fldr2 = folder[i].split('/')
            if not fldr:
                fldr = folder[i].split('/')
                res.append('/'.join(fldr))
            elif fldr != fldr2[:len(fldr)]:
                fldr = fldr2
                res.append('/'.join(fldr))
            i+=1
        return res
