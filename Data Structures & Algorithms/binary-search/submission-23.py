class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1 and nums[0] == target:
            return 0

        l = 0
        r = len(nums) - 1
        mid = r // 2

        for i in range(mid + 2):
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
                mid = (r - l) // 2
            else:
                l = mid
                mid += ((r - l)+1) // 2

        return -1

        