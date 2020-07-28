class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_diff = math.inf
        result = []
        arr.sort()
        for i in range(len(arr)-1):
            min_diff = min(min_diff, abs(arr[i] - arr[i+1]))

        for j in range(len(arr)-1):
            if arr[j+1] - arr[j] == min_diff:
                result.append([arr[j], arr[j+1]])

        return result
