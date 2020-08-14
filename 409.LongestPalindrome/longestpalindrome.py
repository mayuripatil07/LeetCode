class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap = {}
        for i in s:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        flag = 0
        count = 0
        for key, value in hmap.items():
            if value % 2 == 0:
                count += value
            if value % 2 != 0:
                count += value - 1
                flag = 1
        if flag == 1:
            count += 1
        return count
