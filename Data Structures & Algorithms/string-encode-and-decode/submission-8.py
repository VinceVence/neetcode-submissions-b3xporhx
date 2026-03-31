class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += str(len(s)) + "#" + s
        return st

    def decode(self, s: str) -> List[str]:
        k = 0
        res = []
        while k < len(s):
            dig = ""
            i = k
            while s[i] != "#":
                dig += s[i]
                i += 1
            # break
            res.append(s[i + 1: int(dig) + i + 1])
            k = int(dig) + i + 1
        return res

            
