class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        for i in S:
            if i != "#":
                s.append(i)
            elif s and i == "#":
                s.pop()

        t = []
        for i in T:
            if i != "#":
                t.append(i)
            elif t and i == "#":
                t.pop()

        return s == t
