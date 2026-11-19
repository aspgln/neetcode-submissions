# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(root, low, high):
            if not root: 
                return True
            if root.left and ((root.left.val >= root.val) or (root.left.val <= low)):
                return False 
            if root.right and ((root.val >= root.right.val) or (root.right.val >= high)):
                return False 
            else: 
                return (isValid(root.left,low, root.val ) and isValid(root.right, root.val, high))

        if not root: 
            return True 
        

        return isValid(root, float("-inf"), float("inf"))
