class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] * len(deck)
        indx = deque(range(len(deck)))
        print(indx)
        for card in deck:
            i = indx.popleft()
            result[i] = card
            if indx:
                indx.append(indx.popleft())

        return result