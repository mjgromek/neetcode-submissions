class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        waterArea = 0

        while l < r:
            waterArea = max(min(heights[l],heights[r]) * (r - l),waterArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return waterArea


        