class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = collections.defaultdict(list)
        for n in range(len(nums)):
            if nums[n] in hmap:
                hmap[nums[n]].append(n)
            else:
                hmap[nums[n]] = [n]

        for key, value in hmap.items():
            for i in range(1,len(value)):
                if abs(value[i] - value[i-1]) <= k:
                    return True

        return False
