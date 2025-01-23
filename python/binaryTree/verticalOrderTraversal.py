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







rootNode = TreeNode.makeCompleteTreeFromPreOrder([1,2,5,3,4,None,6])
print(TreeNode.makePrettyTree(rootNode))
#print(rootNode)

s = Solution()
res = s.verticalOrder(rootNode)

print(res)