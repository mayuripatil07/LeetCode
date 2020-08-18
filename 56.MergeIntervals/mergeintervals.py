class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        intervals.sort()
        result = [intervals[0]]
        for i in range(1,len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(intervals[i][1], result[-1][1])
            else:
                result.append(intervals[i])
        return result

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key = lambda x : x[0])

        merged.append(intervals[0])
        start = merged[0][0]
        end = merged[0][1]
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:
                end = max(end, interval[1])
                merged[-1][1] = end

            else:
                merged.append(interval)

            end = merged[-1][1]


        return merged
