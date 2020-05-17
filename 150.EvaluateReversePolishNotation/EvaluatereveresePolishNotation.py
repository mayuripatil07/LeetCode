class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        expressions = ['/','*','+','-']
        for token in tokens:
            if token.lstrip('-+').isdigit():
                stack.append(int(token))
            elif token in expressions:
                if len(stack)>= 2:
                    a = stack.pop()
                    b = stack.pop()
                    if token == '*':
                        exp = b * a
                    if token == '/':
                        exp = int(float(b)/a)
                    if token == '+':
                        exp = b + a
                    if token == '-':
                        exp = b - a
                stack.append(exp)

        return stack[-1]

      
