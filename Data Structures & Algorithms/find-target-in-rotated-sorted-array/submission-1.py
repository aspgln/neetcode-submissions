class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first binary search: find the minumim point -> two sorted array 
        # second binary search: find the target value in each sorted array 


        # find minumum point 
        l = 0
        r = len(nums)-1 

        while l < r: 
            if nums[l] <= nums[r]: 
                min_index = l
                min_value = nums[l]
            mid = (l+r)//2 
            if nums[mid] > nums[r]:
                # min in right segment: 
                l = mid + 1 
            elif nums[mid] <= nums[r]:
                r = mid
        min_value = nums[l]
        print(f"l = {l}, min value = {min_value}")

        array_left = nums[:l]
        array_right = nums[l:]
        print(array_left)
        print(array_right)

        def binary_search(array, target):
            print(f"array = {array}")

            if len(array) == 0: 
                return -1
            l = 0
            r = len(array)-1


            if target < array[l] or target > array[r]: 
                    return -1 

            while l <= r: 
                
                mid = (l + r)//2 

                if array[mid] > target: # kept left segment 
                    r = mid -1 
                elif array[mid] < target: # keep right segment
                    l = mid + 1 
                else: 
                    return mid 
            return -1 #  if did not find the value 

        result_l = binary_search(array_left, target)
        result_r = binary_search(array_right, target)

        print(f"result_l: {result_l}")
        print(f"result_r: {result_r}")

        if result_l != -1: 
            return result_l
        
        if result_r != -1: 
            return result_r + l
        
        return -1 




