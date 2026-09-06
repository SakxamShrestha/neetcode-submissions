class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  #this cannot be crowded at all, max size 1 at all times to return True
        hashmap = {')': '(',
                    '}': '{', 
                    ']': '['}

        for c in s:
            if c in hashmap:
                if stack and hashmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False    
            else:
                stack.append(c)       


        return len(stack) == 0                
        