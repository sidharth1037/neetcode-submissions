class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = set()
        for item in nums:
            if item in hmap:
                return True
            else:
                hmap.add(item)
        return False;