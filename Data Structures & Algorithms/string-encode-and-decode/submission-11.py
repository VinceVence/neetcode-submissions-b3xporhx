class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += (str(len(s)) + "#" + s) 
        return st

    def decode(self, s: str) -> List[str]:
        dig = ""
        res = []
        
        i = 0

        while i < len(s):
            dig = ""
            while s[i].isdigit():
                dig+=s[i]
                i += 1
            res.append(s[i+1: i+1+int(dig)])
            i = (i + 1 + int(dig))

        return res


