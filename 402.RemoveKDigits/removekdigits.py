class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and int(i) < int(stack[-1]) and k:
                stack.pop()
                k -= 1
            stack.append(str(i))

        while(k):
            stack.pop()
            k -= 1

        j = 0
        while(j < len(stack) and stack[j] == '0'):
            j += 1

        return ''.join(stack[j:]) if (len(stack[j:]) > 0) else "0"
    
