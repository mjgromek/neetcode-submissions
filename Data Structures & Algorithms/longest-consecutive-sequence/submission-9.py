class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        maxLength = currLength = 0

        for i in range(len(nums)):
            if nums[i] - 1 in nums_set:
                continue
            else:
                element = nums[i]
                while element in nums_set:
                    currLength += 1
                    element += 1

                maxLength = max(maxLength, currLength)
                currLength = 0
        
        return maxLength

        