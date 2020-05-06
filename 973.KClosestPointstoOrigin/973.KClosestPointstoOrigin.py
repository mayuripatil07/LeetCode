class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        result = []
        res = []
        for i in points:
            s = 0
            for j in i:
                s += j**2
            sqrt = s ** 0.5
            res.append((sqrt, i))


        heapq.heapify(res)

        while(res and K>0):
            sqrt, point = (heapq.heappop(res))
            result.append(point)
            K -= 1

        return result
