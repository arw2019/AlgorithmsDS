class Solution:
    def search(self, reader: 'ArrayReader', T: int) -> int:
        L, U = 0, 1
        while T > reader.get(U):
            L, U = U, U*2
        while L <= U:
            M = L + (U-L)//2
            val = reader.get(M)
            if val < T:
                L = M + 1
            elif val == T:
                return M
            else:
                U = M - 1
        return -1
