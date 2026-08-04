class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output_array = []

        for num in nums:
            output_array.append(product)
            product *= num
        
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            output_array[i] *= product
            product *= nums[i]

        return output_array
