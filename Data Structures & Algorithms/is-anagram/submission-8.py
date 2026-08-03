class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1, hash2 = defaultdict(int), defaultdict(int)
         
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hash1[s[i]] += 1
            hash2[t[i]] += 1
        
        return hash1 == hash2