class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        index = 0
        length = ""
        decoded = []
        while index < len(s):
            if s[index] != "#":
                length += s[index]
                index += 1
            else:
                decoded.append(s[index + 1: index + 1 + int(length)])
                index += int(length) + 1
                length = ""
        return decoded

