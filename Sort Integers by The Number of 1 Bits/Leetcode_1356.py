class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        number_of_1_bits = lambda x: bin(x)[2:].count('1') 
        arr_with_1_bit_nos = [(number_of_1_bits(a), a) for a in arr]
        arr_with_1_bit_nos.sort()
        return [a[1] for a in arr_with_1_bit_nos]
