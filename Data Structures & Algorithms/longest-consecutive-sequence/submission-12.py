class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        curr_length = 0
        max_length = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            else:
                curr = num
                while curr in nums_set:
                    curr_length += 1
                    curr += 1
                max_length = max(max_length,curr_length)
                curr_length = 0
        
        return max_length
                
