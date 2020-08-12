class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        for i in range(1,rowIndex+1):
            res = [1]
            for j in range(1, i):
                res.append(result[j-1] + result[j])
            res.append(1)
            result = res
        return result
