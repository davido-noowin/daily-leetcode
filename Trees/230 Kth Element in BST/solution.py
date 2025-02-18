class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest( root: list[TreeNode], k: int) -> int:
    res = []
    def dfs(root):
        if root is None:
            return None
        else:
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

    dfs(root)
    return res[k-1]