class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        hmap = defaultdict(list)
        for i in range(len(nums)):
            hmap[nums[i]].append(i)

        if t == 0:
            for key,value in hmap.items():
                if len(value) > 1:
                    for i in range(len(value)-1):
                        if abs(value[i] - value[i+1]) <= k:
                            return True
            return False

        for i in sorted(hmap.keys()):
            for j in sorted(hmap.keys()):
                if abs(i-j) <= t:
                    for v in hmap[i]:
                        for w in hmap[j]:
                            if 0 < abs(w-v) <= k:
                                return True
        return False
