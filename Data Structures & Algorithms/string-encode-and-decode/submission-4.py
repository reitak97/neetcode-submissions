class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res


    def decode(self, s: str) -> List[str]:
        4#neet4#code
        

        res = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            lenS = int(s[i:j]) #4
            i = j +1
            j = i + lenS
            res.append(s[i:j])
            i = j


        return res




