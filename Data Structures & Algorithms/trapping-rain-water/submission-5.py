class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        prefix = [0 for _ in range(len(height))]
        suffix = [0 for _ in range(len(height))]
        tleft = 0
        tright = -1

        for i in range(len(height)):
            prefix[i] = height[tleft]
            suffix[-(i+1)] = height[tright]
            if height[i]>height[tleft]:
                tleft = i
            if height[-(i+1)]>height[tright]:
                tright = -(i+1)

        print(prefix,'\n',suffix)

        for i in range(len(height)):
            area += max(0,min(prefix[i],suffix[i])-height[i])

        return area
            
            
