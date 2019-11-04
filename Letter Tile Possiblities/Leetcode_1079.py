class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seqs = {''}
        for char in tiles:
            seqs |= {seq[:i] + char + seq[i:] for seq in seqs for i in range(len(seq)+1)}
        return len(seqs)-1
