class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        L = len(heights)
        l = 0
        r = L-1 
        output = 0

        while l < r: 
            area = min(heights[l], heights[r]) * (r-l)  
            # print(f"l,r = {l},{r}, heights = {heights[l]},{heights[r]}, area = {area}")

            if area > output: 
                output = area 
            if heights[l] > heights[r]: 
                r = r-1 
            else: 
                l = l+1
        return output


