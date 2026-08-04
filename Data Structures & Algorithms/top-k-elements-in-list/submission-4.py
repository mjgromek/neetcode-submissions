class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        buckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq[num] += 1
        
        for key, value in freq.items():
            buckets[value].append(key)
        
        res = []
        for i in range(len(buckets) - 1, -1,-1):
            if len(buckets[i]) != 0:
                for bucket in buckets[i]:
                    res.append(bucket)
                    if len(res) == k:
                        return res


        