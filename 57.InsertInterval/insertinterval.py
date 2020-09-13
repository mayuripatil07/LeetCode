class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        sorted_interval = sorted(intervals, key = lambda x:x[0])
        result = [sorted_interval[0]]
        for i in range(1, len(sorted_interval)):
            b = sorted_interval[i]
            a = result[-1]

            if a[1] >= b[0]:
                a[1] = max(b[1], a[1])
            else:
                result.append(b)

        return result
