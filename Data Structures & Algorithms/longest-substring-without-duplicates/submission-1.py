class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l,r, count,maxCount = 0, 0, 0, 0

        while l <= r and r < len(s):

            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                    count -= 1
            
            seen.add(s[r])
            count += 1

            maxCount = max(count,maxCount)
            r += 1
        
        return maxCount