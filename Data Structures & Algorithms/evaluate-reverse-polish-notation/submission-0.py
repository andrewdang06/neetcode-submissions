class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        a, b = 0, 0
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))

            elif token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))

        return stack[0]        

            
        