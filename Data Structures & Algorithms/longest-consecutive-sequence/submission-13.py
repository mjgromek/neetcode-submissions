class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        curr_length = 0
        max_length = 0
        curr = 0

        for num in nums_set:
            if not num - 1 in nums_set:
                curr = num
                while num in nums_set:
                    curr_length += 1
                    num += 1
                max_length = max(max_length, curr_length)
                curr_length = 0
        return max_length

            

        