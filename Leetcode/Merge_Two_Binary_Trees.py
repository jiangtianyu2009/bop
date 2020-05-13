class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        t0 = TreeNode(0)
        if (not t1) and (not t2):
            return None
        else:
            if (not t1) and t2:
                return t2
            elif t1 and (not t2):
                return t1
            else:
                t0.val = t1.val + t2.val
                t0.left = self.mergeTrees(t1.left, t2.left)
                t0.right = self.mergeTrees(t1.right, t2.right)
                return t0
