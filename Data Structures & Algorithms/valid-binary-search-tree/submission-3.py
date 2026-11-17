# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True 
        
        q = collections.deque()
        q.append([root,float("-inf"),float("inf") ])


        while q: 
            node, leftb, rightb = q.popleft()
            if not leftb < node.val < rightb: 
                return False
            else: 
                if node.left: 
                    q.append([node.left, leftb, node.val])
                if node.right: 
                    q.append([node.right, node.val, rightb])
        return True 