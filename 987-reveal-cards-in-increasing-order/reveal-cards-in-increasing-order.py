class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] * len(deck)
        queue = deque(range(len(deck)))

        for num in deck:
            index = queue.popleft()
            result[index] = num
            if queue:
                queue.append(queue.popleft())
        
        return result