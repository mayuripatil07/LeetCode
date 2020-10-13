class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        rem = 0
        rev = 0
        while(x):
            rem = x % 10
            x  = x//10
            rev = 10 * rev + rem

        if neg:
            rev = - rev
        if abs(rev) > (2**31 - 1):
            return 0
        return rev
