import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sw = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return(sw[::-1] == sw)

        