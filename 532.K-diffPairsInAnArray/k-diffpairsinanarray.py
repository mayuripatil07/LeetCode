class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = set()
        count = 0
        if k == 0:
            for i in nums:
                x = nums.count(i)
                if x > 1:
                    res.add((i,i))
        elif k > 0:
            for i in range(len(nums)):
                if nums[i] - k in nums:
                    res.add((nums[i], nums[i]-k))


        return len(res)
        
