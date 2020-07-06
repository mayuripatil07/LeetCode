class Solution:
    def customSortString(self, S: str, T: str) -> str:
        s = ""
        S_hmap = collections.OrderedDict()
        for ch in range(len(S)):
            S_hmap[ch] = S[ch]

        for key, value in S_hmap.items():
            if value in T:
                c = T.count(value)
                s += value * c
        for i in T:
            if i not in s:
                c1 = T.count(i)
                s+= i * c1
        return s
