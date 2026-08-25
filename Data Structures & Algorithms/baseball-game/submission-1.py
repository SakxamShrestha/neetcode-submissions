class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []

        for c in operations: 
            if c == "+":
                # Add the sum of the last two elements
                stack.append(stack[-1] + stack[-2])
            elif c == "D":
                # Double the last element
                stack.append(stack[-1] * 2)
            elif c == "C":
                # Invalidate (remove) the last element
                stack.pop() # Wait, just stack.pop() is enough!
            else:
                # If it's not a special char, it must be a number
                # This handles negative numbers like "-5" correctly
                stack.append(int(c))

        return sum(stack)