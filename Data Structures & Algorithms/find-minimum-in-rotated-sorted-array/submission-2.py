class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums)-1
        answer = nums[0]

        while l < r: 
            if nums[l] <= nums[r]:
                answer = nums[l]

            mid = (l+r)//2

            # compare mid vs. right 

            if nums[mid] <= nums[r]: # keep left segment, including mid 
                r = mid 
                answer = nums[l]
            elif nums[mid] >  nums[r]: # keep right segment, exclude mid
                l = mid + 1
                answer = nums[mid]

        return nums[l] 
