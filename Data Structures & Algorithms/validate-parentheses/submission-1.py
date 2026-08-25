class Solution:
    def isValid(self, s: str) -> bool:
        #making a hashmap where we link the closing parentheses 
        #with the opening parentheses and pushing everything 
        #in the stack, and have to make sure that we should close
        #the brackets in the correct order in here. 
        #for that, we have to use stack, and always check for the 
        #top most element on the stack, if we find the exat opening bracket,
        # we pop it from the stack, and we only become successful 
        #if the stack is empty at last.... 


        res_stack = []
        hashmap = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        #iterating through the elements of the string 

        for c in s:
            if c in hashmap:
                if res_stack and res_stack[-1] == hashmap[c]:
                    res_stack.pop()
                else:
                    return False    
            else:
                res_stack.append(c)

        print(res_stack)

        if len(res_stack) == 0:
            return True 
        else:
            return False                    

        