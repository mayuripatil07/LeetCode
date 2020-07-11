class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr = []
        max_profit = 0
        for i in range(len(difficulty)):
            arr.append((profit[i], difficulty[i]))
        arr.sort(reverse = True)
        worker.sort(reverse = True)
        i = 0
        j = 0
        while(i < len(worker) and j < len(arr)):
            if worker[i] >= arr[j][1]:
                max_profit += 1 * arr[j][0]
                i += 1
            elif worker[i] < arr[j][1]:
                j += 1
        return max_profit
