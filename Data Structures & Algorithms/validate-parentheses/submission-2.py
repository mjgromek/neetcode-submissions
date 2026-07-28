class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = ["()","{}","[]"]
        pairs = set(pairs)

        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif (stack[-1] + s[i]) in pairs:
                stack.pop()
            else:
                stack.append(s[i])
        
        return True if len(stack) == 0 else False
        