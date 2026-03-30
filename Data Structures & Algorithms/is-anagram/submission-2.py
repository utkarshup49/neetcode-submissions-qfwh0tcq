class Solution:
    def isAnagram(self, s: str, t: str):
        length_s= len(s)
        length_t = len(t)
        if length_s != length_t:
            return False
        return sorted(s) == sorted(t)
        