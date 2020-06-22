class Solution:
    def minIncrementForUnique(self, result: List[int]) -> int:
        result.sort()
        count = 0

        for i in range(1,len(result)):
            if result[i-1] >= result[i]:
                initial = result[i]
                result[i] = result[i-1] + 1
                count += result[i] - initial
        return count
