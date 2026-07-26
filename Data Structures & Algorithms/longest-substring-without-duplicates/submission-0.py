class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        seen = set()
        count = 0

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
            
            count = max(count,right - left + 1)
            right += 1
        
        return count
