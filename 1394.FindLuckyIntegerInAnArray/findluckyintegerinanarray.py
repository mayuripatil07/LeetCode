class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a = Counter(arr)
        largest_num = -1
        for key,value in a.items():
            if key == value:
                largest_num = max(largest_num, key)

        return largest_num
