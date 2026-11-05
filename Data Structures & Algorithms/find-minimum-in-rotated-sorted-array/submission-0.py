class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = len(nums)

        left = 0
        right = L-1 
        answer = nums[left]
        print(f"start, answer = {answer}")

        while left <= right: 
            print(f"----------------")
            print(f"left={left}, right={right}, leftN={nums[left]}, rightN={nums[right]}")

            if nums[left] <= nums[right]:
                print(f"finish searching")
                answer = min(answer, nums[left] )
                break 

            else: 
                print(f"current array: {nums[left:right+1]}")

                mid = (left + right) // 2 
                print(f"mid={mid}, midN={nums[mid]}")
                answer = min(answer, nums[mid] )

                if nums[mid] < nums[left]: 
                    right = mid -1 
                    print(f"keep left segment: {nums[left:right+1]}")

                elif nums[mid] >= nums[right]:
                    left = mid + 1 
                    print(f"keep right segment: {nums[left:right+1]}")
                    
                
        return answer 










        if L == 1: 
            return nums[0]

        # while L > 1:

        #     if l <= mid and mid < r: 
        #         answer = nums[l]
        #         return answer 
        #     elif l > mid and mid < r: # deflectioni point on the left side 
        #         l = l 
        #         r = mid 
        #         mid = (l+r)//2
        #         nums = nums[l:r]
        #         L = len(nums)

        #     elif l <= mid and mid >= r: # defectio on the right side 
        #         l = mid
        #         r = r
        #         mid = (l+r)//2
        #         nums = nums[l:r]
        #         L = len(nums)

        return answer 