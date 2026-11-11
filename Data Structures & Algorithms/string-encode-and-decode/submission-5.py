class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s 
        return res

        #res = "5#Hello5#World"
                
    def decode(self, s: str) -> List[str]:
        res = []
        #two pointers to extract len
        i = 0
        

        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = s[i:j]
            j +=1
            i = j + int(length)
            res.append(s[j:i])
        return res

            
