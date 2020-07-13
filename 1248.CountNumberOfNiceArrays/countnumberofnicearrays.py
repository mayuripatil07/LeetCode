class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        total = 0
        count = 0
        for i in range(len(nums)):
            if(nums[i]%2==0):
                nums[i] = 0
            else:
                nums[i] = 1

        trackTotal = {0:1}
        for i in range(len(nums)):
            total+=nums[i]
            if(total - k in trackTotal):
                count+=trackTotal[total-k]
            if total in trackTotal:
                trackTotal[total] += 1
            else:
                trackTotal[total] = 1
        return count
