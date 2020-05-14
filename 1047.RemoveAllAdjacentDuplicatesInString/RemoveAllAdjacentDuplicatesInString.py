class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i in S:
            if len(stack) == 0:
                stack.append(i)
            elif i != stack[-1]:
                stack.append(i)
            elif  i == stack[-1]:
                stack.pop()

        return "".join(stack)
            
