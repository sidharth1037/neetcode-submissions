class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = set(nums)
        smallest = None
        longest = 1 if len(nums) else 0

        for item in nums:
            if item-1 in hmap:
                continue
            else:
                length = 1
                while item+1 in hmap:
                    length += 1
                    item +=1
                longest = max(longest,length)
        
        return longest