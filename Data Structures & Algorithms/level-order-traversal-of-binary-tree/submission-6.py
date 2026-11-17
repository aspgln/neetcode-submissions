# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        q = collections.deque()
        q.append(root)
        if not root: 
            return []

        while q: 
            level = []
            level_size = len(q)

            for _ in range(level_size):
                # step1: pop left of q an add to level 
                # step 2: add child to q
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                    
                if node.right: 
                    q.append(node.right)

            results.append(level)
        return results 