from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        m1 = defaultdict(int)
        m2 = defaultdict(int)

        for item in s:
            m1[item] += 1

        for item in t:
            m2[item] += 1

        if m1==m2:
            return True
        else:
            return False