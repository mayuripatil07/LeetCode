class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        final = sum(A) + sum(B)
        final = final // 2
        reqA = final - sum(A)
        s = set(B)
        for a in A:
            if a + reqA in s:
                return [a,a+reqA]
