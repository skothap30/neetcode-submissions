class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        operations = ["-", "+", "*", "/"]
        for token in tokens:
            if token in operations:
                first = res.pop(-1)
                second = res.pop(-1)
                if token == '-':
                    res.append(second - first)
                elif token == '+':
                    res.append(first + second)
                elif token == '*':
                    res.append(first * second)
                elif token == '/':
                    res.append(int(second / first))
            else:
                res.append(int(token))
        return res[-1]