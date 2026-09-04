class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #value = index 

        for i, n in enumerate(nums): #enumerate helps us to go through index and the number at once.
            diff = target - n 
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n] = i     

        