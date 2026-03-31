class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = defaultdict(list)

        for l in strs:
            charset = [0] * 26
            for s in l:
                charset[ord(s) - ord("a")] += 1
            c[tuple(charset)].append(l)
        return(list(c.values()))
        