class Solution:
    def decodeString(self, s: str) -> str:
        digit = ""
        stack = []
        prev = ''
        alpha = ''
        for i in s:
            if i.isdigit():
                digit += i
            if i == '[':
                stack.append((int(digit), alpha))
                digit = ""
                alpha = ""
            if i == ']':
                num, prev = stack.pop()
                alpha = prev + (alpha * num)
            if i.isalpha():
                alpha += i
        return alpha

         
