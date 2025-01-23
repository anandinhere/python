from util.binarytreeutil import TreeNode



from typing import Optional, List

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        cols = {}

        def set_cols(root, index,height) -> None:

            if root is None:
                return
            if index not in cols:
                cols[index] = [(root.val,height)]
            else:
                cols[index].append(root.val)

            set_cols(root.left,index-1,height+1)
            set_cols(root.right,index+1,height+1)

        #cols.sort()

        set_cols(root,0,0)
        #sorted_dict = dict(sorted(cols.items()))
        sorted_values = [value for key, value in sorted(cols.items())]
        #vals = []


        return sorted_values


    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:

        q1 = []
        q2 = []
        res = []

        q1.append(root)

        while q1 or q2:

            while len(q1) > 0:

                node = q1.pop(0)

                res.append(node.val) if node is not None else res.append(None)
                if not node:
                    continue
                if node.left or node.right:
                    q2.append(node.left)
                    q2.append(node.right)

            while len(q2) > 0:

                node = q2.pop(0)

                res.append(node.val) if node is not None else res.append(None)
                if not node:
                    continue
                if node.left or node.right:
                    q1.append(node.left)
                    q1.append(node.right)

        return res

rootNode = TreeNode(1)
rootNode.left = TreeNode(2)
rootNode.left.left = TreeNode(3)
rootNode.left.right = TreeNode(4)
rootNode.right = TreeNode(5)
rootNode.right.right = TreeNode(6)

print(TreeNode.makePrettyTree(rootNode))
#print(rootNode)

s = Solution()
res = s.levelOrder(rootNode)

print(res)