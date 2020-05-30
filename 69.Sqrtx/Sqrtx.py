class Solution:
    def mySqrt(self, x: int) -> int:
        if x <2 :
            return x

        low = 1
        high = x //2
        while(low <= high):
            mid = (low + high) // 2
            num = mid * mid
            if num == x:
                return mid
            elif num > x:
                high = mid - 1
            elif num < x:
                low = mid + 1
        return high
                
