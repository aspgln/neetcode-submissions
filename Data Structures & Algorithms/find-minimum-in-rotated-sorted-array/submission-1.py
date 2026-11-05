class Solution:
    def findMin(self, nums) -> int:

        l = 0
        r = len(nums)-1

        answer = nums[0]

        while l <= r: 
            if nums[l] <= nums[r]:
                answer = min(answer,nums[l])
                break


            mid = (l+r)//2 
            answer = min(answer, nums[mid])

            if nums[mid] < nums[l]: # keep left segment
                r = mid - 1
            elif nums[mid]  > nums[r]: # keep right segment
                l = mid + 1 
                

        return answer
