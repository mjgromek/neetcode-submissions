class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = []
        suffix_array = []
        output_array = []
        prev = post = 1

        for i in range(len(nums)):
            prefix_array.append(prev)
            prev *= nums[i]

            suffix_array.append(post)
            post *= nums[len(nums) - i-1]

        for i in range(len(nums)):
            output_array.append(prefix_array[i]*suffix_array[len(nums)-i-1])
        
        return output_array