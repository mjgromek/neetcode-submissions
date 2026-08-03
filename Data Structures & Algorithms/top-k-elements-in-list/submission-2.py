class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for i in range(len(nums) + 1)]
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        for key, value in freq.items():
            buckets[value].append(key)
        
        result = []
        for i in range(len(buckets)-1,0,-1):
            if len(buckets[i]) != 0:
                for j in range(len(buckets[i])):
                    result.append(buckets[i][j])
                    if len(result) == k:
                        return result


        