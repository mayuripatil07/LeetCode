class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        for idx, c in enumerate(citations):
            if idx >= c:
                return idx
        return len(citations)
