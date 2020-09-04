from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        lst = []
        A.sort()
        for i in permutations(A,4):
            lst.append("".join(map(str,i)))
        lst1 = [x for x in lst if int(x[:2])<24 and int(x[2:])<60]
        if len(lst1) == 0:
            return ""
        ans = lst1[-1]
        return (ans[:2]+":"+ans[2:])
