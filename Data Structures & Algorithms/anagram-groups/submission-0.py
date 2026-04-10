class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = {}

        for item in strs:
            key = [0]*26
            for ch in item:
                key[ord(ch)-ord('a')] += 1
            hmap.setdefault(tuple(key), []).append(item)

        return list(hmap.values())