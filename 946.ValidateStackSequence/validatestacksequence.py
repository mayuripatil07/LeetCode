class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        j = 0
        while(j < len(pushed)):
            if stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
            else:
                stack.append(pushed[j])
                j += 1

        while i < len(popped):
            if stack[-1] == popped[i]:
                stack.pop()
                i += 1
            else:
                return False
        return True
