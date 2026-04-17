from collections import deque

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        lsum = [1]
        product = 1

        for i in range(1,len(nums)):
            product *= nums[i-1]
            lsum.append(product)

        rsum = deque([1])
        product = 1

        for i in range(len(nums)-2,-1,-1):
            product *= nums[i+1]
            rsum.appendleft(product)

        for i in range(len(nums)):
            ans.append(lsum[i]*rsum[i])

        return ans