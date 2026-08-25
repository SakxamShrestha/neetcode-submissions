class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        l = 0
        longest = 0
        
        for r in range(len(s)):
            # 1. Shrink window from the left if s[r] is a duplicate
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1
            
            # 2. Add the new, non-duplicate character
            unique_chars.add(s[r])

            print(unique_chars)
            
            # 3. Update longest (current window length is r - l + 1)
            longest = max(longest, r - l + 1)
            
        return longest