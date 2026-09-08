class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #I think this is we go through the tokens put everything in stack (numbers) and once we find any operators we pop the stack, evaluate the result, and put the result back in the stack again, until what reamins in the stack is our answer and wew return it. 
        stack = []
        result = 0
        for t in tokens: 
            if t not in "+-*/":
                stack.append(int(t))
            else:
                b = stack.pop()    
                a = stack.pop()
                if t == "+":
                    result = a + b
                elif t == "-":
                    result = a - b
                elif t == "*":
                    result = a * b
                elif t == "/":
                    result  = int(a / b)
                stack.append(result)


        return stack[-1]                      