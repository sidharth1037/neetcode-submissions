class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}

        for i,item in enumerate(nums):
            if item in hmap:
                return [hmap[item],i]
            else:
                hmap[target-item] = i