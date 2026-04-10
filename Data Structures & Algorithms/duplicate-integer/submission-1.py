class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for item in nums:
            if item in hmap:
                return True
            else:
                hmap[item] = True
        return False;