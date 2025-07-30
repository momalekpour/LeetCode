# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Solution
## Time complexity: O(H), where H is the height of the tree.
## Space complexity: O(H) for the recursion stack.
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # target node has 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # target node has 2 childern
            else:
                # find a most-left (smallest) node in right sub-tree
                curr = root.right
                while curr and curr.left:
                    curr = curr.left
                min_val_node = curr
                root.val = min_val_node.val
                root.right = self.deleteNode(root.right, min_val_node.val)

        return root
