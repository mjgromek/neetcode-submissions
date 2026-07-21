class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()

        for i in range(len(nums)):
            print(i)
            if (target - nums[i]) in seen:
                print(seen,target - nums[i] )
                return [min(i,nums.index(target - nums[i])),max(i,nums.index(target - nums[i]))]
            seen.add(nums[i])