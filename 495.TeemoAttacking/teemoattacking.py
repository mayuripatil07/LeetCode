class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        poison_time = timeSeries[0] + duration
        poison_condition = duration
        for i in range(1,len(timeSeries)):
            if poison_time <= timeSeries[i]:
                poison_condition += duration
                poison_time = timeSeries[i] + duration
            elif poison_time > timeSeries[i]:
                diff = poison_time - timeSeries[i]
                add_time = duration - diff
                if diff <= duration:
                    poison_condition += add_time
                poison_time = timeSeries[i] + duration
        return poison_condition
