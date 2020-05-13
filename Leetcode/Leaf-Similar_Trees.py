# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def buildTree(self, elemlist):
        nodelist = []
        for elem in elemlist:
            nodelist.append(TreeNode(elem))
        i = 0
        wiza = True
        for j in range(1, len(nodelist)):
            if wiza:
                if nodelist[j].val is not None:
                    nodelist[i].left = nodelist[j]
            else:
                if nodelist[j].val is not None:
                    nodelist[i].right = nodelist[j]
                i = i + 1
            wiza = not wiza
        return nodelist[0]


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        root1_list = []
        root2_list = []
        self.getleaf(root1, root1_list)
        self.getleaf(root2, root2_list)
        print(root1_list)
        print(root2_list)
        isequ = True
        for i in range(len(root1_list)):
            if root1_list[i] != root2_list[i]:
                isequ = False
        return isequ

    def getleaf(self, root, root_list):
        if root.left == root.right == None:
            root_list.append(root.val)
        elif root.right == None:
            self.getleaf(root.left, root_list)
        elif root.left == None:
            self.getleaf(root.right, root_list)
        else:
            self.getleaf(root.left, root_list)
            self.getleaf(root.right, root_list)


if __name__ == '__main__':
    print(Solution().leafSimilar(Tree().buildTree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
                                 Tree().buildTree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])))
