class Solution:
    def calculate(self, s: str) -> int:
        tokens = re.findall(r'\d+|\+|\-|\+|\*|\/', s)
        stack = []
        symbol = '+'
        for i in tokens:
            if i.isdigit():
                if symbol == '+':
                    stack.append(int(i))
                if symbol == '-':
                    stack.append(-1 * int(i))
                if symbol == '*':
                    stack.append(int(stack.pop()*int(i)))
                if symbol == '/':
                    stack.append(int(stack.pop() / float(int(i))))
            else:
                symbol = i
        return int(sum(stack))
