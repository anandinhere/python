class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ptr1 = 0
        ptr2 = 1
        max_len = 1
        str_len = len(s)

        if str_len <= 1:
            return str_len

        uniq_items_map = {}

        # while ptr less than str lenght, add items to map if the map doesn't already contain same item and index greater than start ptr1
        # increment pointer
        # if while condition exits, if ptr2 still less than str len, clear map. reset start position to 1 index after duplicate item
        # add item to map only if item not already in map
        uniq_items_map.update({s[ptr1]: ptr1})
        while ptr2 < str_len:
            if s[ptr2] in uniq_items_map and uniq_items_map[s[ptr2]] >= ptr1 and uniq_items_map[s[ptr2]] != ptr2:
                item_index = uniq_items_map[s[ptr2]]
                uniq_items_map.update({s[ptr2]: ptr2})
                curr_len = ptr2 - item_index
                max_len = max(max_len, curr_len)
                ptr1 = item_index + 1
                ptr2 = ptr1 + 1
            else:
                uniq_items_map.update({s[ptr2]: ptr2})
                curr_len = ptr2 - ptr1 + 1
                max_len = max(max_len, curr_len)
                ptr2 += 1

        return max_len



print(Solution().lengthOfLongestSubstring("dvdf"))