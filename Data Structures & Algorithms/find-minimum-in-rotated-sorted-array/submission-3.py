class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1 

        answer = nums[l]

        while l < r: 
            # if nums[l] <= nums[r]:
            #     answer = nums[l]
                
            # answer = nums[l]
            mid = (r+l)//2 
            print(f"l,mid, r = {l}, {mid}, {r}")

            if nums[mid] > nums[r]: 
                l = mid + 1
            elif nums[mid] <= nums[r]: 
                r = mid
            
            answer = nums[l]
        return answer 
