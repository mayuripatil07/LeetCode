class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            fn, typ, time = log.split(':')

            if typ == 'start':
                if stack:
                    res[stack[-1]] += int(time) - prev_time
                stack.append(int(fn))
                prev_time = int(time)
            else:
                res[stack.pop()] += int(time) - prev_time + 1
                prev_time = int(time) + 1

        return res
