class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        buckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq[num] += 1
        
        for key,count in freq.items():
            buckets[count].append(key)

        output_array = []

        for i in range(len(buckets)-1,0,-1):
            if len(buckets[i]) != 0:
                for j in range(len(buckets[i])):
                    output_array.append(buckets[i][j])
                    if len(output_array) == k:
                        return output_array
                    



        