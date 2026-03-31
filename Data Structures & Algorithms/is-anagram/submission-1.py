class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = {} # a
        d2 = {} # b
        for a,b in zip(s,t):
            if a not in d1:
                d1[a] = 0
            else:
                d1[a] += 1

            if b not in d2:
                d2[b] = 0
            else:
                d2[b] += 1
        return d1 == d2
            
        