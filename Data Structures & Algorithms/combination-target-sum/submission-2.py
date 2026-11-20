class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        def dfs(i, curr, total):
            if total == target:
                results.append(curr.copy())
                return 
            
            if i >= len(nums) or total > target: 
                return 
            
            candidate = nums[i]
            curr.append(candidate)
            # print(f"tried [{curr}]")
            dfs(i, curr, total + candidate)
            curr.pop()
            dfs(i +1, curr, total)
            # print(f"tried [{curr}]")

        dfs(0,[],0)

        return results
