# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS
    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, totalSum: int = 0) -> bool:
        if not root:
            return False
        totalSum += root.val

        if not root.left and not root.right:
            return totalSum == targetSum
        if self.hasPathSum(root.left, targetSum, totalSum):
            return True
        if self.hasPathSum(root.right, targetSum, totalSum):
            return True

        totalSum -= root.val
        return False
