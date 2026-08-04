class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:

        decoded = []
        length = ""
        index = 0

        while index < len(s):
            if s[index] == "#":
                decoded.append(s[index + 1: index + 1 + int(length)])
                index += int(length)   
                length = ""
            else:
                length += s[index]

            index += 1
        
        return decoded
            
