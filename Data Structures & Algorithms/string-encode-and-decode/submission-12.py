class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        
        length_str = ""
        index = 0
        decoded = []
        while index < len(s):
            while s[index]!= "#":
                length_str += s[index]
                index += 1
            decoded.append(s[index + 1: index + 1 + int(length_str)])
            index += 1 + int(length_str)
            length_str = ""
        return decoded



