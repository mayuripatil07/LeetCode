class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == 0:
            return [-1]
        result = []
        res = []
        for i in arr:
            diff = abs(x - i)
            res.append((diff, i))

        heapq.heapify(res)

        while(res and k > 0):
            diff, num = heapq.heappop(res)
            result.append(num)
            k -= 1
        result.sort()
        return result
            
