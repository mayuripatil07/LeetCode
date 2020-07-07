class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res = set()
        l = len(A[0])
        c_even = []
        c_odd = []
        for i in A:
            for j in range(l):
                if j % 2 == 0 :
                    c_even.append(i[j])
                else:
                    c_odd.append(i[j])

            c_even.sort()
            c_odd.sort()
            res.add("".join(c_even + c_odd))
            c_even.clear()
            c_odd.clear()

        return len(res)
