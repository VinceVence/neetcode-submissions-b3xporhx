class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""

        for s in strs:
            st += (str(len(s)) + "#" + s) 
        return st

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num = ""
            while s[i].isdigit():
                num += s[i]
                i+=1
            res.append(s[i + 1 : int(num) + i + 1])
            i = int(num) + i + 1
        print(res)
        return res
                
            