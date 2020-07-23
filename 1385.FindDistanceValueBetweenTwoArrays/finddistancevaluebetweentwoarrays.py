class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = []
        for i in range(len(arr1)):
            flag = 0
            for j in range(len(arr2)):
                diff = abs(arr1[i] - arr2[j])
                if diff <= d:
                    flag = 1
                    break
            if not flag:
                res.append(diff)

        return len(res)
    
