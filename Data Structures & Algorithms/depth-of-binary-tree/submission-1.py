# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS 
        if not root:
            return 0
        depth = 0

        stack = [(root,1)]

        while stack:
            node, current_depth = stack.pop()

            if node:
                depth = max(depth, current_depth)

                stack.append((node.left, current_depth + 1))
                stack.append((node.right, current_depth + 1))


        return depth                

        