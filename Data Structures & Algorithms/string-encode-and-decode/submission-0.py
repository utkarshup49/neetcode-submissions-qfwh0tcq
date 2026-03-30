class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for a in strs:
            b = len(a)
            s+= str(b) + "@" + a
        return s

        


    def decode(self, s: str) -> List[str]:
        main = []
        i,j = 0,0
        print(s)
        print(len(s))
        while i < len(s):
            while s[j] != "@":
                j+=1
            length = int(s[i:j])
            start = j+1
            end = start + length
            word = s[start:end]
            main.append(word)

            i = end
            j = i
        print(main)
        return main

