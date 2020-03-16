from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:        
        res = [0]*(len(barcodes))
        i = 0
        for barcode, freq in Counter(barcodes).most_common():
            for _ in range(freq):
                res[i] = barcode
                i += 2
                if i >= len(barcodes): i=1
        return res
