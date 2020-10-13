class Solution:
    def isPalindrome(self, x: int) -> bool:
        prev_x = x
        if x < 0:
            return False
        rev = 0
        rem = 0
        while(x):
            rem = x % 10
            x = x //10
            rev = rev * 10 + rem
        diff = rev - prev_x
        if diff == 0:
            return True
        else:
            return False
