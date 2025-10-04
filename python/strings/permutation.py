



def getLexicographicRank(input) -> int:


    sorted_input = sorted(input)
    print(sorted_input)

    ranked_chars = { c:i+1 for i,c in enumerate(sorted_input) }
    print(ranked_chars)




    def get_rank(i):

        if i==0:
            return 0
        if i ==1:
            return i
        return i * get_rank(i-1)

    res = 0
    for i,c in enumerate(input):
        sort_position = ranked_chars[c]
        max_chars_less_than_c = sort_position - 1
        chars_possible = min(max_chars_less_than_c, len(input)-i-1)

        rank_except_this = get_rank(len(input)-i-1)


        res = res + (chars_possible * rank_except_this)
        print(res,sort_position)


    return res + 1


print(getLexicographicRank('string'))