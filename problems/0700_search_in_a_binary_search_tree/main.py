# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. Recursion
# Time complexity: O(H)
# Space complexity: O(H) for recursion stack.
# Where H is the height of the given tree. (H = log(n) for balanced tree and n for skewed tree.)
class Solution:
    def searchBST(self, root: TreeNode, target):
        if not root:
            return False
        if root.val > target:
            return self.searchBST_2(self, root.left, target)
        elif root.val < target:
            return self.searchBST_2(self, root.right, target)
        else:
            return True

    # less verbose version
    # def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #     if not root or root.val == val:
    #         return root
    #     return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)


# 2. Iteration
# Time complexity: O(H)
# Space complexity: O(1)
# Where H is the height of the given tree. (H = log(n) for balanced tree and n for skewed tree.)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root
