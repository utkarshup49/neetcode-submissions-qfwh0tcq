from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]):
        #{key:value,key:value}
        hashm = defaultdict(list)
        result = []
        for s in strs:
            sorted_s = tuple(sorted(s))
            hashm[sorted_s].append(s)

        for v in hashm.values():
            result.append(v)
        return result    
        