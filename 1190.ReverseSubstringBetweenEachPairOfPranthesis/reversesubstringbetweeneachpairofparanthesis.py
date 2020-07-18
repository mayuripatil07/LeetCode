class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for i in s:
            if i == '(':
                stack.append([])
            elif i == ')':
                word = stack.pop()
                stack[-1].extend(word[::-1])
            else:
                stack[-1].append(i)

        return ''.join(stack.pop())
