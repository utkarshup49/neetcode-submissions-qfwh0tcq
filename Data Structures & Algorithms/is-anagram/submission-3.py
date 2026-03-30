class Solution:
    def isAnagram(self, s: str, t: str):
        length_s= len(s)
        length_t = len(t)
        if length_s != length_t:
            return False
        countS = {}
        countT = {}
        for i in range(length_s):
            countS[s[i]] =  1 + countS.get(s[i],0)
            countT[t[i]] =  1 + countT.get(t[i],0)
        return countS == countT
        