class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        result = []
        min_diff = math.inf
        for time in timePoints:
            h, m = time.split(":")
            min_ = int(h)*60 + int(m)
            result.append(min_)

        result.sort()
        result.append(result[0])

        for i in range(1,len(result)):
            diff = abs(result[i] - result[i-1])
            min_diff = min(diff, min_diff, 24*60-diff)

        return min_diff
