
from util import bitutil
from typing import List
class Anangram:
    def __init__(self):
        self.dummy = None

    def check_numbers_are_binary_anagrams(self, num1:int, num2:int) -> bool:


        bitutil.get_binary_repr(num1)
        bitutil.get_binary_repr(num2)


        no_of_1s_in_num1 = bitutil.count_1s(num1)
        no_of_1s_in_num2 = bitutil.count_1s(num2)

        return no_of_1s_in_num1==no_of_1s_in_num2

    def anagrams_together(self,words:List) -> List[List[str]]:

        anagram_map = {}

        for word in words:
            if str(sorted(word)) not in anagram_map:
                anagram_map[str(sorted(word))] = [word]
            else:
                anagram_map[str(sorted(word))].append(word)

        res = []
        for vals in anagram_map.values():
            res.append(vals)

        return res



a = Anangram()
print(a.check_numbers_are_binary_anagrams(9,8))
print(a.anagrams_together(["cat", "dog", "tac", "god", "act", "ogd"]))