class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for i in S:
            if stack and stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)

        return len(stack)
