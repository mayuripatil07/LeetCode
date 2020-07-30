class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        hmap = {0 : 1}
        count = 0
        s = 0
        for i in range(len(A)):
            s += A[i]
            if s % K in hmap:
                count += hmap[s % K]
                hmap[s%K] += 1
            else:
                hmap[s%K] = 1
        return count


            
