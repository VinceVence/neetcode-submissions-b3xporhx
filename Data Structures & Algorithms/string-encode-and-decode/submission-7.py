class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += (str(len(s)) + "#" + s)
        print(st)
        return st

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            dig = ""
            j = i
            while s[j].isdigit():
                dig += s[j]
                j += 1
            print(s[j+1 : int(dig) + j + 1])
            res.append(s[j+1 : int(dig) + j + 1])
            i = int(dig) + j + 1
            print(res)
        return res


