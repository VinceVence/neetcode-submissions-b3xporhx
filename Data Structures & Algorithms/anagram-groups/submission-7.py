class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for st in strs:
            charset = [0] * 26
            
            for s in st:
                charset[ord(s) - ord("a")] += 1
            d[tuple(charset)].append(st)
        return (list(d.values()))            