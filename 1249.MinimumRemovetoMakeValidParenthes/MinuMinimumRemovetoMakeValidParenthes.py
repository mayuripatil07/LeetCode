class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_count = 0
        stack = []
        invalid = []
        st = list(s)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    invalid.append(i)

        invalid = stack + invalid

        for i in invalid:
            st[i] = ""

        return "".join(st)
        
