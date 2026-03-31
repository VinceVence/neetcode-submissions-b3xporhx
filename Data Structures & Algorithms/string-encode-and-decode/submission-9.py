class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += (str(len(s)) + "#" + s)
        return st

    def decode(self, s: str) -> List[str]:
        l = 0
        res = []

        while l < len(s):
            dig = ""
            while s[l].isdigit():
                dig += s[l]
                l += 1
            print(dig)
            print(s[l+1 : l + int(dig) + 1])
            res.append(s[l+1 : l + int(dig) + 1])
            l = (l + int(dig) + 1)
        return res