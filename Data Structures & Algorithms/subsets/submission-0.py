from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # This list will store all the final subsets. It's the answer we'll return.
        res = [] 
        
        # This list acts as the "current" subset we are building during the recursion.
        # It gets modified (added to and removed from) as we explore possibilities.
        subset = []

        # This is the core recursive function, often called a "backtracking" function.
        # The parameter 'i' represents the index of the number in 'nums' we are currently considering.
        def dfs(i):
            
            # --- BASE CASE ---
            # If our index 'i' is out of bounds, it means we have made a decision
            # (either include or not include) for every number in the input 'nums'.
            # The current state of 'subset' is a complete, valid subset.
            if i >= len(nums):
                # We add a *copy* of the current subset to our result list.
                # It MUST be a copy because 'subset' will be modified later as we backtrack.
                # If we didn't copy, all entries in 'res' would point to the same list.
                res.append(subset.copy())
                return # Stop this path of recursion and go back up.

            # --- RECURSIVE STEPS (The Decision Tree) ---
            
            # Decision 1: INCLUDE the element nums[i]
            # ----------------------------------------
            # Add the current number to our temporary subset.
            subset.append(nums[i])
            # Explore further down this path by calling dfs for the *next* number.
            dfs(i + 1)

            # Decision 2: DO NOT INCLUDE the element nums[i] (This is the "backtrack" step)
            # -----------------------------------------------------------------------------
            # Now, we "undo" the decision we made above by removing the element.
            # This brings 'subset' back to the state it was in before we included nums[i],
            # allowing us to explore the other path where we don't include it.
            subset.pop()
            # Explore the other path where we skip nums[i] by calling dfs for the next number.
            dfs(i + 1)

        # Start the recursion from the beginning of the list (index 0).
        dfs(0)
        
        # After the recursion has explored all possible paths, return the final list of subsets.
        return res