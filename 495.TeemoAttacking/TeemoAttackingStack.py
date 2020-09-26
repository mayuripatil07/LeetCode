class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries or duration == 0:
            return 0
        stack = [timeSeries[0] + duration]
        count = duration
        for time in range(1,len(timeSeries)):
            if stack and stack[-1] > timeSeries[time]:
                diff = stack[-1] - timeSeries[time]
                add_time = duration - diff
                if diff <= duration:
                    count += add_time
                   
            elif stack and stack[-1] <= timeSeries[time]:
                count += duration
            poison_time = timeSeries[time] + duration
            stack.append(poison_time)
       
        return count
    
