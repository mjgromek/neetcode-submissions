class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = defaultdict(int)
        maxCount,count,l = 0,0,0

        for r in range(len(s)):
            res[s[r]] += 1
            count += 1
            while (r - l + 1) - max(res.values()) > k:
                res[s[l]] -= 1
                l += 1
                count -= 1
            maxCount = max(maxCount,count)
        
        return maxCount
