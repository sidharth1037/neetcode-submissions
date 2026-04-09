class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}

        for i,item in enumerate(nums):
            if item not in hmap:
                hmap[target-item] = i
            else:
                return [hmap[item],i]