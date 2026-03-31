class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s: 
            if c in ["(", "[", "{"]:
                stack.append(c)
            elif len(stack) > 0:
                if stack[-1] == "(" and c == ")": stack.pop()
                elif stack[-1] == "[" and c == "]": stack.pop()
                elif stack[-1] == "{" and c == "}": stack.pop()
                else: return False
            else:
                return False
        return True if len(stack) == 0 else False
        