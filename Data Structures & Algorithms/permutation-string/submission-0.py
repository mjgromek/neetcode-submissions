class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freq1 = [0] * 26
        for s in s1:
            freq1[ord(s) - ord("a")] += 1
        

        l,r = 0,0
        freq2 = [0] * 26
        while r < len(s2):
            while r - l != len(s1) and r < len(s2):
                freq2[ord(s2[r]) - ord("a")] += 1
                r += 1
            if freq1 == freq2:
                return True
            else:
                freq2[ord(s2[l]) - ord("a")] -= 1
                l += 1

        return False


