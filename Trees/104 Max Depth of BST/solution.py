class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(self, root: list[TreeNode]) -> int:
    def dfs(root):
        if root is None:
                return 0
        else:
            return 1 + max(dfs(root.left), dfs(root.right))

    return dfs(root)