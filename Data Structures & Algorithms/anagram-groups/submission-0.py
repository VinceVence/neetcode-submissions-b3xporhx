class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)
        charset = [0] * 26
        for st in strs:
            charset = [0] * 26
            for c in st:
                charset[ord(c) - ord('a')] += 1
            d[tuple(charset)].append(st)
        print(d)
        #     if d[tuple(charset)] not in d.keys():
        #         d[tuple(charset)] = list(st)
        #     else: 
        #         d[tuple(charset)].append(st)
        return list(d.values())
        