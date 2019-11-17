from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        dq = deque()
        for card in sorted(deck, reverse=True):
            dq.rotate()
            dq.appendleft(card)
        return list(dq)
