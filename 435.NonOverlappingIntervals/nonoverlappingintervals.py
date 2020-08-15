class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals == []:
            return 0
        intervals.sort()
        result = [intervals[0]]
        count = 0
        for i in range(1,len(intervals)):
            if result[-1][1] > intervals[i][0]:
                last_interval = min(result[-1][1], intervals[i][1])
                result[-1][1] = last_interval
                count += 1
            else:
                result.append(intervals[i])
        return count 
