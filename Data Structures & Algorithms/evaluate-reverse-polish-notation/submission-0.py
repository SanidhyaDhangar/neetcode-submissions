class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                r = stack.pop()
                l = stack.pop()
                if tokens[i] == "+":
                    res = l + r
                if tokens[i] == "/":
                    res = int(l / r)
                if tokens[i] == "-":
                    res = l - r
                if tokens[i] == "*": 
                    res = l * r
                stack.append(res)
        return stack[-1]