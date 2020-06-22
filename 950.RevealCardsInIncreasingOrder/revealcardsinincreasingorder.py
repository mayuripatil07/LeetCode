class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = deque()
        result.append(deck.pop())

        while(deck):
            result.append(result.popleft())
            result.append(deck.pop())

        return reversed(result)
