class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        nx = sum(s1[i]!=s2[i] and s1[i]=='x' for i in range(len(s1)))
        ny = sum(s1[i]!=s2[i] and s1[i]=='y' for i in range(len(s1)))
        return -1 if (nx-ny)%2 else nx//2 + ny//2 + 2*(nx%2)
