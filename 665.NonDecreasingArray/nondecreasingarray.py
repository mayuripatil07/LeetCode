class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        c = 0
        p = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                c += 1
                p = i + 1
        if c == 0:
            return True
        elif c > 1:
            return False
        else:
            if p == 1 or p == len(nums) - 1:
                return True
            else:
                return ((nums[p - 1] <= nums[p + 1]) or (nums[p - 2] <= nums[p])) 
