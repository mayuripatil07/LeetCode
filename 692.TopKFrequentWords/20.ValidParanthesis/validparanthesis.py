class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'}':'{', ')':'(', ']': '['}
        st = []
        for i in s:
            if i in hmap.values():
                st.append(i)
            elif i in hmap.keys():
                if len(st) == 0 or st.pop() != hmap[i]:
                    return False

        return st == []
