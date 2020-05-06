class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        result = []
        heapq.heapify(sticks)

        while(len(sticks) > 1):
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            s = a+b
            result.append(s)
            heapq.heappush(sticks, s)

        return sum(result)
