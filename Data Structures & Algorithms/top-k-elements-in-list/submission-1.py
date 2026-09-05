class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        buckets = [[] for _ in range(len(nums) + 1)] # to initialize shallow buckets
        
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
            #or one liner is hashmap.get(n, 0) + 1

        for num, count in hashmap.items():
            buckets[count].append(num)

        result = []    
        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result      

        