class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        for i in range(len(s)-1,-1,-1):
            if s[i-1] < s[i]:
                index = i - 1
                break

        if i <= 0:
            return -1

        diff = math.inf
        for j in range(index+1, len(s)):
            if s[index] < s[j] and int(s[j]) - int(s[index]) < diff:
                diff = int(s[j]) - int(s[index])
                swap_index = j

        s[index], s[swap_index] = s[swap_index], s[index]

        ans = ''.join(s[:index+1] + sorted(s[index + 1:]))
        return ans if int(ans) < 2**31 else -1
