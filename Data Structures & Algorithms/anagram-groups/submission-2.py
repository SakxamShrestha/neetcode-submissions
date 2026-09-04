class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #thought process is using hashmaps to count character frequency, but how would we know from hashmaps on which anagarams to store independently??? 
        hashmap = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            key = tuple(count)

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(s)

        return list(hashmap.values())            
