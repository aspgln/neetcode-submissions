class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        pivot = l
        # find the pivot point 
        while l <= r: 

            mid = (l+r)//2 

            if nums[l] == nums[r]: 
                pivot = l
                break 
            
            if nums[mid] < nums[r]: 
                r = mid 
            else: 
                l = mid+1 
            pivot = l
        
        print(f"pivot={pivot}, value = {nums[pivot]}")

        nums_left = nums[:pivot]
        nums_right = nums[pivot:]

        def binary_search(array, target):
            l,r = 0,len(array)-1

            if not array: 
                return -1

            if target > array[-1] or target < array[0]: 
                return -1 

            while l <= r: 
                mid = (l+r)//2
                if array[mid] == target: 
                    return mid
                elif array[mid] < target: 
                    l = mid + 1 
                else: 
                    r = mid-1

            return -1 
        
        # print(nums_left)
        # print(nums_right)

        out1 = binary_search(nums_left, target)
        # print(out1)

        if out1 == -1: 
            out2 = binary_search(nums_right, target)
            # print(out2)

            if out2 == -1: 
                return -1
            else:
                 return out2 + pivot 
        else: 
            return out1
