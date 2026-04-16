from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ""
        for item in strs:
            coded += str(len(item)) + '#' + item
        return coded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])            
            j += 1
            
            word = s[j:j + length]
            res.append(word)            
            i = j + length

        return res