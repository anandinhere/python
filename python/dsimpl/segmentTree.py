
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



make_tree(0,len(nums)-1, 0,nums,s_tree)
print(s_tree)

#[45, 10, 35, 3, 7, 18, 17, 1, 2, 3, 4, 11, 7, 8, 9, 0, 1, 0, 0, 0, 0, 0, 0, 5, 6, 0, 0, 0, 0, 0, 0, 0]
#[45, 10, 35, 3, 7, 18, 17, 1, 2, 3, 4, 11, 7, 8, 9, 0, 1, 0, 0, 0, 0, 0, 0, 5, 6, 0, 0, 0, 0, 0, 0]
