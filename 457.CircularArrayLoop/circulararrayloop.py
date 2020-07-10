class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        l = len(nums)

        for i in range(l):
            if nums[i] == 0:
                continue

            flag = False
            if nums[i] > 0:
                flag = True

            s = set()
            j = i
            start = i
            while(j not in s):
                if nums[j] > 0 and not flag:
                    break
                elif nums[j] < 0 and flag:
                    break

                s.add(j)
                j = j + nums[j]
                j = (j + l)%l
                if j == start:
                    if len(s) <= 1:
                        break
                    return True
        return False
