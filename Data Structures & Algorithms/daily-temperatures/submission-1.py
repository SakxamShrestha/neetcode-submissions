class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # so for this, we have to make sure than i+1 temperatures are a bit warm than previous, then only we can do plus one in the relevant index of the list. so we first initilize an empty list with zeros with no of index (no of tiem) same as of in the temperatures list. so how do we acheive this using stack??? 
        res = [0] * len(temperatures)

        stack = []

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)    

        return res    


        