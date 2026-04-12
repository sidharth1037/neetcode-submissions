class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        freq = [[] for _ in range(len(nums)+1)]

        for item in nums:
            hmap[item] = hmap.get(item,0) + 1

        for key, count in hmap.items():
            freq[count].append(key)

        ans = []
        for i in range(len(freq)-1,0,-1):
            for item in freq[i]:
                ans.append(item)
                if len(ans)==k:
                    return ans
        return ans