import itertools
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        a = [1,2,3,4,5,6,7,8,9]
        comb = itertools.combinations(a, k)
        for x in comb:
            if sum(x) == n:
                result.append(list(x))
        return result
