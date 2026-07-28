class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = set(["+","-","*","/"])

        for token in tokens:
            if token in operators:
                elem1 = stack.pop()
                elem2 = stack.pop()
                match token:
                    case "+":
                        stack.append(elem1 + elem2)
                    case "-":
                        stack.append(elem2 - elem1)
                    case "*":
                        stack.append(elem1*elem2)
                    case "/":
                        stack.append(int(elem2/elem1))
            else:
                stack.append(int(token))
        return stack[-1]
        