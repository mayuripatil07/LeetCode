class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        hmap = {0:1}
        count = 0
        s = 0
        for i in A:
            s += i
            if s - S in hmap:
                count += hmap[s-S]
            if s in hmap:
                hmap[s] += 1
            else:
                hmap[s] = 1

        return count
