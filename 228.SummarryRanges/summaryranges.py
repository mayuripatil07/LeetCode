class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        result = []
        while(i < len(nums)-1):
            res = []
            flag = 0
            while(i < len(nums) - 1 and nums[i] + 1 == nums[i+1]):
                res.append(nums[i])
                flag = 1
                i += 1
            if flag:
                res.append(nums[i])
                result.append((str(res[0]) + '->' + str(res[-1])))

                i += 1
            else:
                result.append(str(nums[i]))
                i += 1
        if i == len(nums)-1:
            result.append(str(nums[i]))
        return result
            
