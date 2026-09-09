class Solution:
    def isPalindrome(self, s: str) -> bool:
        #we need to create a function by ourselves mayb isalnum which will help us detect if we have alphanumeric charscters or not in our string. 

        l , r = 0, len(s) - 1
        while l < r:
            while l < r and self.isalnum(s[l]) is not True:
                l += 1
            while l < r and self.isalnum(s[r]) is not True:
                r -= 1


            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1


        return True  

    def isalnum(self,c):
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))    

        # we are not storing anything so maybe  constant space but big O of n time complexity in here optimally.     

        