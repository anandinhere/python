
class Palindrome:

    def __init__(self):
        self.dummy = None

    def checkPalindrome(self,input:str) -> bool:

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

p = Palindrome()
l = [('anana',True), ('anand',False), ('',True), (None,True)]
for a,b in l:
    assert p.checkPalindrome(a) == b, f"Failed for input: {a}"