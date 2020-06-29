class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        res = []
        for i in range(len(mat)):
            freq = mat[i].count(1)
            result.append((freq, i))

        result.sort()
        for i in range(k):
            res.append(result[i][1])
        return res
