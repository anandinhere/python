
from typing import Optional

class Palindrome:

    def __init__(self):
        self.dummy = None

    def checkPalindrome(self,input:str) -> bool:

        print(input)
        if input is None or len(input) <=1:
            return True

        start = 0
        end = len(input) - 1

        while start <= end:
            if input[start] != input[end]:
                return False
            start += 1
            end -= 1

        return True

    def longestPalindromicSubsequence(self,input:str) -> int:


        print(input)
        if input is None:
            return 0

        length = len(input)
        if length <= 1:
            return length

        def compute(start, end, input, length):

            if start < 0 or end >= length or start > end:
                return 0

            if start == end:
                return 1



            if input[start] == input[end]:
                val =  2 + compute(start+1, end-1, input, length)
                #print(val)
                return val
            else:
                val = max(compute(start, end-1, input, length),compute(start+1, end, input, length))
                #print(val)
                return val


        val =  compute(0,length-1,input,length)
        print(val)
        return val

    def longestPalindromicSubstringLength(self,input:str) -> int:


        print(input)
        if input is None:
            return 0

        length = len(input)
        if length <= 1:
            return length

        def compute(start, end, input, length, curr):

            if start < 0 or end >= length or start > end:
                return curr

            if start == end:
                return curr + 1


            if input[start] == input[end]:
                return compute(start+1, end-1, input, length, curr + 2)
                #print(val)
            else:
                val = max(compute(start, end-1, input, length,0),compute(start+1, end, input, length,0))
                #print(val)
                return val


        val =  compute(0,length-1,input,length, 0)
        print(val)
        return val

    def longestPalindromicSubstring(self, input) -> Optional[str]:

        if input is None or len(input) <=1:
            return input

        i_len = len(input)

        max_len = 0
        res = ''

        for start in range(i_len):

            for end in range(i_len-1,start-1,-1):

                flag = True
                s = start
                e = end

                while s <= e:
                    if input[s] != input[e]:
                        flag = False
                        break
                    s += 1
                    e -= 1
                curr_len = end-start+1
                if flag and curr_len > max_len:
                    res = input[start:end+1]
                    max_len = curr_len

        return res

    def longestPalindromicSubstringn2(self, input) -> Optional[str]:

        if input is None or len(input) <=1:
            return input

        i_len = len(input)

        return None





p = Palindrome()
l = [('anana',True), ('anand',False), ('',True), (None,True)]
# for i in l:
#     assert p.checkPalindrome(i[0]) == i[1], f"Failed for input: {i[0]}"



test_cases = [
    # Basic cases
    ("bba", 2),  # Longest palindromic subsequence is "bbbb"
    ("bbbb", 4),  # Longest palindromic subsequence is "bbbb"
    ("bbbab", 4),  # Longest palindromic subsequence is "bbbb"
    ("a", 1),  # Single character is itself a palindrome
    ("racecar", 7),  # Entire string is already a palindrome

    # Non-palindromic and mixed cases
    ("abcde", 1),  # No repeating characters, so longest is any single character
    ("agbdba", 5),  # Longest palindromic subsequence is "abdba"

    # Repeated characters
    ("aaaa", 4),  # All characters are the same, so the entire string is the LPS

    # Edge cases
    ("", 0),  # Empty string has no subsequences
    ("ab", 1),  # No palindrome longer than a single character
    ("aa", 2),  # Both characters are the same, forming a palindrome

    # Mixed characters
    ("character", 5),  # Longest palindromic subsequence is "carac"

    # Case-sensitive tests
    ("AaAa", 3),  # Case-sensitive: LPS is "AaA" (ignoring the mismatched 'a')
    ("AbcBA", 3),  # Case-sensitive: LPS is "ABA" (skipping mismatched 'c' and case differences)

    # Palindrome with embedded noise
    ("abaxyzzyxf", 6),  # Longest palindromic subsequence is "xyzzyx"

    # Long and repetitive string
    ("aabbccdd", 2),  # LPS is either "aa", "bb", "cc", or "dd"
    ("aabcdcb", 5),  # LPS is "abcdcba"

    # Large test case (for performance validation)
    ("abcd" * 5, 9),  # Longest palindromic subsequence is any single character
]
#
# for i in test_cases:
#     assert p.longestPalindromicSubsequence(i[0]) == i[1], f"Failed for input: {i[0]}"


test_cases = [
    # Format: (input_string, expected_length)

    # Basic cases
    ("babad", 3),  # Longest palindromic substring is "bab" or "aba"
    ("cbbd", 2),   # Longest palindromic substring is "bb"

    # Single character
    ("a", 1),      # Single character is a palindrome
    ("z", 1),      # Single character is a palindrome

    # Entire string is a palindrome
    ("racecar", 7),  # The entire string is already a palindrome
    ("aaaa", 4),     # All characters are the same, so the entire string is the LPS

    # Edge cases
    ("", 0),        # Empty string has no palindromic substring
    ("ab", 1),      # Longest palindromic substring is any single character
    ("aa", 2),      # The entire string is a palindrome

    # Mixed cases
    ("character", 3),  # Longest palindromic substring is "ara"
    ("forgeeksskeegfor", 10),  # Longest palindromic substring is "geeksskeeg"

    # Embedded palindromes
    ("abaxyzzyxf", 6),  # Longest palindromic substring is "xyzzyx"
    ("abcdadcba", 9),   # The entire string is the LPS

    # Long and repetitive strings
    ("aabbccddeeff", 2),  # Any repeated pair works, e.g., "aa", "bb"
    ("aabcdcb", 5),       # Longest palindromic substring is "bcdcb"

    # Case sensitivity
    ("AaAa", 3),         # Case-sensitive: LPS is "AaA"
    ("AbcbA", 5),        # The entire string is a palindrome
]


# for i in test_cases:
#     assert p.longestPalindromicSubstringLength(i[0]) == i[1], f"Failed for input: {i[0]}"


test_cases = [
    # Format: (input_string, expected_output)

    # Basic cases
    ("babad", "bab"),  # "aba" is also a valid result, but one of them suffices
    ("cbbd", "bb"),    # Longest palindromic substring is "bb"

    # Single character
    ("a", "a"),        # Single character is a palindrome
    ("z", "z"),        # Single character

    # Entire string is a palindrome
    ("racecar", "racecar"),  # The entire string is already a palindrome
    ("aaaa", "aaaa"),        # All characters are the same, so the entire string is the LPS

    # Edge cases
    ("", ""),               # Empty string has no palindromic substring
    ("ab", "a"),            # Either "a" or "b" is a valid answer
    ("aa", "aa"),           # The entire string is the palindrome

    # Mixed cases
    ("character", "ara"),   # Longest palindromic substring is "ara"
    ("forgeeksskeegfor", "geeksskeeg"),  # Symmetry in the middle

    # Embedded palindromes
    ("abaxyzzyxf", "xyzzyx"),  # Longest palindromic substring is "xyzzyx"
    ("abcdadcba", "abcdadcba"),  # The entire string is the LPS

    # Long and repetitive strings
    ("aabbccddeeff", "aa"),  # Any repeated pair works, e.g., "bb", "cc"
    ("aabcdcb", "bcdcb"),    # Longest palindromic substring is "bcdcb"

    # Case sensitivity
    ("AaAa", "AaA"),         # Case-sensitive: Longest substring is "AaA"
    ("AbcbA", "AbcbA"),      # The entire string is a palindrome
]


for i in test_cases:

    assert p.longestPalindromicSubstring(i[0]) == i[1], f"Failed for input: {i[0]}"