class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        stack = [0]
        for i in range(0,len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                    res[stack.pop()] = i - stack[-1]
            stack.append(i)
        return res
          
