class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_array = []
        product = 1

        for i in range(len(nums)):
            output_array.append(product)
            product *= nums[i]
        
        product = 1
        for i in range(len(nums)-1,-1,-1):
            output_array[i] *= product
            product *= nums[i]

        return output_array

