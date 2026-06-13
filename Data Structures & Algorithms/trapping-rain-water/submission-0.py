class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax = height[l]
        rmax = height[r]
        water = 0
        while l < r:
            if lmax < rmax:
                l += 1
                if height[l] < lmax:
                    water += lmax - height[l]
                else:
                    lmax = height[l]
            else:
                r -= 1
                if height[r] < rmax:
                    water += rmax - height[r]
                else:
                    rmax = height[r]
        return water