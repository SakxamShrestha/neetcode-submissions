class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1, hash2 = {}, {}

        for x in s: 
            if x not in hash1:
                hash1[x] = 1
            hash1[x] += 1

        for c in t: 
            if c not in hash2:
                hash2[c] = 1
            hash2[c] += 1 

        if hash1 == hash2:
            return True  
        else:
            return False       

        