class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(' ')
        arr = list(filter(None, arr))
        if not arr:
            return 0
        return len(arr[-1])
