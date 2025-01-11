
from util import bitutil
class Anangram:
    def __init__(self):
        self.dummy = None

    def check_numbers_are_binary_anagrams(self, num1:int, num2:int) -> bool:


        bitutil.get_binary_repr(num1)
        bitutil.get_binary_repr(num2)


        no_of_1s_in_num1 = bitutil.count_1s(num1)
        no_of_1s_in_num2 = bitutil.count_1s(num2)

        return no_of_1s_in_num1==no_of_1s_in_num2



a = Anangram()
print(a.check_numbers_are_binary_anagrams(9,8))