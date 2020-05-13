class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = collections.defaultdict(int)
        result = []
        for i in nums:
            hmap[i] += 1

        heap = [(-freq, element) for element, freq in hmap.items()]
        heapq.heapify(heap)

        while(heap and k > 0):
            freq, element = heapq.heappop(heap)
            result.append(element)
            k -= 1

        return result
