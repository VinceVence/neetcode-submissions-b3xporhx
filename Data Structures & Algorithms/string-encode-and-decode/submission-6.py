class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += f"{len(s)}" + "#" + s
        return st 

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i
            dig = ""

            while s[j].isdigit():
                dig += s[j]
                j += 1

            res.append(s[j + 1 : int(dig) + j + 1])
            print(res)
            i = int(dig) + j + 1
        return res


