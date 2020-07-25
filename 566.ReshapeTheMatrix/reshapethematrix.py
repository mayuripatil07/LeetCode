class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(nums) * len(nums[0]):
            return nums
        res = []
        matrix = [[0] * c for _ in range(r)]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                res.append(nums[i][j])
        R = r - 1
        while(R >= 0):
            C = c - 1
            while(C >= 0):
                matrix[R][C] = res.pop()
                C -= 1
            R -= 1
        return matrix
