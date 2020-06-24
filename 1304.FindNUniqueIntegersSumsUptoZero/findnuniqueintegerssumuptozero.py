class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2 != 0:
            result.append(0)
            n = n - 1
        r = n // 2
        for i in range(1,r+1):
            result.append(i)
            result.append(-1*i)

        return result
                
