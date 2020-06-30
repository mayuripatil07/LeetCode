class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res1 = []
        res2 = []
        res = []
        for i in range(n):
            res1.append(nums[i])

        for i in range(n, len(nums)):
            res2.append(nums[i])

        for i in range(len(res1)):
            res.append(res1[i])
            res.append(res2[i])

        return res
            
