class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        for char in s:
            if char in hashS:
                hashS[char] += 1
            else:
                hashS[char] = 0

        for char in t:
            if char in hashT:
                hashT[char] += 1
            else:
                hashT[char] = 0

        return hashS == hashT

        