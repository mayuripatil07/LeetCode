class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        while(i <= len(nums) - 1):
            if nums[i] != i + 1:
                j = nums[i] - 1
                while(nums[i] != i + 1 and nums[i] != nums[j]):
                    j = nums[i] - 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1

        for i in range(len(nums)):
            if nums[i] != i +1:
                result.append(i+1)

        return result
            
