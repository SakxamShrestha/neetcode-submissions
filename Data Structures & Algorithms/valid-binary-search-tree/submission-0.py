# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 
        res, stack, curr = [], [], root

        while curr or stack:
            while curr:
                stack.append(curr)

                if curr.left and curr.left.val > curr.val:
                    return False 
                curr = curr.left    

            curr = stack.pop()

            if res and curr.val <= res[-1]:
                return False
            res.append(curr.val)
            curr = curr.right    

        return True                 
                
        