

class CharCount:
    def __init__(self):
        self.dummy = None


    def count_words(self,sentence:str,) -> int:

        clean_str = ''
        for c in sentence:
            if c.isalnum() or c.isspace():
                clean_str += c

        words = clean_str.split()
        print(words)

        return len(words)

    def smallestWindowsOfChars(self, s:str, t:str) -> None:
        chars_hash = {}
        char_count = len(t)
        for c in t:
            if c in chars_hash:
                chars_hash[c] += 1
            else:
                chars_hash[c] = 1

        curr_start = None
        curr_end = None

        res_start = None
        res_end = None
        min_window = len(s) + 1
        res_chars_hash = {}
        res_char_count = 0


        for i, c in enumerate(s):

            if c in chars_hash and chars_hash[c] > 0:
                if curr_start is None:
                    curr_start = i
                if c not in res_chars_hash:
                    res_chars_hash[c] = 1
                else:
                    res_chars_hash[c]+=1
                if res_chars_hash[c] <= chars_hash[c]:
                    res_char_count += 1

            if res_char_count == char_count:
                if curr_end is None:
                    curr_end = i
                min_window = min(min_window,curr_end-curr_start+1)


                while curr_start <= i:
                    char_at_curr_start = s[curr_start]
                    if char_at_curr_start not in chars_hash or \
                            res_chars_hash[char_at_curr_start] > chars_hash[char_at_curr_start]:
                        curr_start += 1
                        if char_at_curr_start in chars_hash:
                            res_chars_hash[char_at_curr_start] -= 1
                        curr_end = i
                        temp_window = min(min_window,curr_end-curr_start+1)
                        if temp_window <min_window:
                            min_window = temp_window
                            res_start = curr_start
                            res_end = curr_end
                    else:
                        break



        print(s[res_start:res_end+1])





        return None





c = CharCount()
print(c.count_words('One two          three\n four\t five\n  '))

print(c.smallestWindowsOfChars('this is a test string', 'tist'))