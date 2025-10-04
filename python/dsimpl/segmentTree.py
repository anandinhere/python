

from util.binarytreeutil import TreeNode
nums = [ i for i in range(0,10)]





def get_next_2_power(num):


    if (num & num -1) == 0:
        return num

    v = 0
    while num!=0:
        num = num >> 1

        v += 1

    return 2 ** v

s_tree_len = (2 * get_next_2_power(len(nums))) - 1



s_tree = [0 for i in range(s_tree_len)]



def make_tree(in_start, in_end, r_start, nums,s_tree) -> int:



    if in_start == in_end:
        s_tree[r_start] = nums[in_start]
        return nums[in_start]

    r_mid = (r_start * 2) + 1
    in_mid = (in_start + in_end)//2

    s_tree[r_start] = make_tree(in_start,in_mid,r_mid,nums,s_tree) + make_tree(in_mid+1,in_end,r_mid+1,nums,s_tree)

    return s_tree[r_start]


#get sum of subtrees
def get_sum(range_start, range_end, nums_start, nums_end, r_start, nums, s_tree) -> int:

    if range_start == nums_start and range_end == nums_end:
        return s_tree[r_start]


    r_mid = (r_start * 2) + 1
    nums_mid = (nums_start + nums_end) // 2




    if range_start <= nums_mid and nums_mid < range_end: #first call for range_start <= nums_mid 2nd call for nums_mid < range_end
        return get_sum(range_start, nums_mid, nums_start, nums_mid, r_mid, nums, s_tree) + \
               get_sum(nums_mid + 1, range_end, nums_mid + 1, nums_end, r_mid + 1, nums, s_tree)
    elif range_end <= nums_mid: #because im considering nums mid
        return get_sum(range_start, range_end, nums_start, nums_mid, r_mid, nums, s_tree)
    else:
        return get_sum(range_start, range_end, nums_mid + 1, nums_end, r_mid + 1, nums, s_tree)



make_tree(0,len(nums)-1, 0,nums,s_tree)
print(s_tree)

root = TreeNode.makeCompleteTreeFromPreOrder(s_tree)

prettyTree = TreeNode.makePrettyTree(root)

prettyTree.pprint()
#[45, 10, 35, 3, 7, 18, 17, 1, 2, 3, 4, 11, 7, 8, 9, 0, 1, 0, 0, 0, 0, 0, 0, 5, 6, 0, 0, 0, 0, 0, 0, 0]
#[45, 10, 35, 3, 7, 18, 17, 1, 2, 3, 4, 11, 7, 8, 9, 0, 1, 0, 0, 0, 0, 0, 0, 5, 6, 0, 0, 0, 0, 0, 0]

range_sum =  get_sum(0,6,0,len(nums)-1, 0,nums,s_tree)
print(range_sum)

