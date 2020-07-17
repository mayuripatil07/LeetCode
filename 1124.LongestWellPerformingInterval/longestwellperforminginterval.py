class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        pos = {}
        s, max_len = 0, 0

        for i in range(len(hours)):
            if hours[i] > 8:
                s += 1
            else:
                s -= 1

            if s > 0:
                max_len = max(max_len, i+1)
            else:
                p = s-1
                if p in pos:
                    max_len = max(max_len, i-pos[p])

            if s not in pos:
                pos[s] = i

        return max_len
                s
