class Solution:
    def isValid(self, s: str) -> bool:
        b = []
        for char in s:
            if char in ['[', '(', '{']:
                b.append(char)

            else:
                if len(b) > 0:
                    if char == "]" and b[-1] == "[": b.pop()
                    elif char == ")" and b[-1] == "(": b.pop()
                    elif char == "}" and b[-1] == "{": b.pop()
                    else: return False
                else:
                    return False
        return True if len(b) == 0 else False
        