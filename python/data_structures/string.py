

print(f'''

https://www.digitalocean.com/community/tutorials/python-string-functions#python-string-functions


format()	It’s used to create a formatted string from the template string and the supplied values.
s = 'testString {{}} {{}}'
print(s.format('hi','hello'))
''')



s = 'testString {} {}'


print(s.format('hi','hello'))



print(f'''
s = 'Nov 7 2025 9:35:000'
split_date = s.split(sep=' ',maxsplit=4)
split_time = split_date[3].split(sep=':')
        ''')

s = 'Nov 7 2025 9:35:000'

split_date = s.split(sep=' ',maxsplit=4)
split_time = split_date[3].split(sep=':')
print(f'split_date {split_date} \nsplit time {split_time}')


print(f"join()	This function returns a new string that is the concatenation of the strings in iterable with string object as a delimiter.")
s= ['Nov' , '7' , '2025']
s_join = '-_-'.join(s)
print(f'''
s= ['Nov' , '7' , '2025']
s_join = '-_-'.join(s)
''')
print(s_join)


print(f'''strip()	Used to trim whitespaces from the string object.
        s = '   hi    '
        print(s.strip())''')

s = '   hi    '
print(s.strip())


s = '1 {one} 2 {two} 345'
m = { 'one' : 'a', 'two': 'b', '3': 'c', '4':'d', '5' : 'e'}
print(f'''format_map()	Python string format_map() function returns a formatted version of the string using substitutions from the mapping provided.
        s = '12345'
        m = {{ '1' : 'a', '2': 'b', '3': 'c', '4':'d', '5' : 'e'}}
        print(s.format_map(m)

person_data = {{'name': 'Alice', 'age': 30}}
formatted_string = "Name: {{name}}, Age: {{age}}.".format_map(person_data)
print(formatted_string) ''')

print(s.format_map(m))


person_data = {'name': 'Alice', 'age': 30}
formatted_string = "Name: {name}, Age: {age}.".format_map(person_data)
print(formatted_string)



print(f'''
    replace()	Python string replace() function is used to create a new string by replacing some parts of another string.
    s = 'one two three one twp four five six five'
    print(s.replace('one' , 'ten', 2))
        ''')

s = 'one two three one twp four five six five'
print(s.replace('one' , 'ten', 2))


print(f'''
    find()	Python String find() method is used to find the index of a substring in a string.
    s = 'one two three one two four five six five'
    print(s.find('three',0,20)))

    index()	Python String index() function returns the lowest index where the specified substring is found.
    In Python, the str.index() and str.find() methods are used to locate the position of a substring within a 
    string, and in many cases, they return the same result. However, their behavior when the substring is not found is the key difference: 


        ''')
s = 'one two three one two four five six five'
print(s.find('three',0,20))


print(f'''
    translate()	Python String translate() function returns a new string with each character 
    in the string replaced using the given translation table.

    s = 'abcde'
    translation_table = str.maketrans('ab', '12')
    print(translation_table)
    print(s.translate(translation_table))
    ''')

s = 'abcde'
translation_table = str.maketrans('ab', '12')
print(translation_table)
print(s.translate(translation_table))


all_functions = r'''







upper()	We can convert a string to uppercase in Python using str.upper() function.
lower()	This function creates a new string in lowercase.


Good to Know String Functions

Function	Description
encode()	Python string encode() function is used to encode the string using the provided encoding.
count()	Python String count() function returns the number of occurrences of a substring in the given string.
startswith()	Python string startswith() function returns True if the string starts with the given prefix,                        otherwise it returns False.
endswith()	Python string endswith() function returns True if the string ends with the given suffix, otherwise it           returns False.
capitalize()	Python String capitalize() function returns the capitalized version of the string.
center()	Python string center() function returns a centered string of specified size.
casefold()	Python string casefold() function returns a casefolded copy of the string. This function is used to perform case-insensitive string comparison.
expandtabs()	Python string expandtabs() function returns a new string with tab characters (\t) replaced with one or more whitespaces.
__contains__()	Python String class has __contains__() function that we can use to check if it contains another string or not. We can also use “in” operator to perform this check.


Miscellaneous String Functions


str.isdigit() and str.isnumeric()
 both check if a string contains only numeric characters, but 
 isnumeric() is more inclusive of various Unicode number representations. 


Function	Description
isalnum()	Python string isalnum() function returns True if it’s made of alphanumeric characters only.
isalpha()	Python String isalpha() function returns True if all the characters in the string are alphabets, otherwise False.
isdecimal()	Python String isdecimal() function returns True if all the characters in the string are decimal characters, otherwise False.
isdigit()	Python String isdigit() function returns True if all the characters in the string are digits, otherwise False.
isidentifier()	Python String isidentifier() function returns True if the string is a valid identifier according to the Python language definition.
islower()	Python String islower() returns True if all cased characters in the string are lowercase and there is at least one cased character, otherwise it returns False.
isnumeric()	Python String isnumeric() function returns True if all the characters in the string are numeric, otherwise False. If the string is empty, then this function returns False.
isprintable()	Python String isprintable() function returns True if all characters in the string are printable or the string is empty, False otherwise.
isspace()	Python String isspace() function returns True if there are only whitespace characters in the string, otherwise it returns False.
istitle()	Python String istitle() returns True if the string is title cased and not empty, otherwise it returns False.
isupper()	Python String isupper() function returns True if all the cased characters are in Uppercase.
rjust(), ljust()	Utility functions to create a new string of specified length from the source string with right and left justification.
swapcase()	Python String swapcase() function returns a new string with uppercase characters converted to lowercase and vice versa.
partition()	Python String partition() function splits a string based on a separator into a tuple with three strings.
splitlines()	Python String splitlines() function returns the list of lines in the string.
title()	Python String title() function returns a title cased version of the string.
zfill()	Python String zfill(width) function returns a new string of specified width. The string is filled with 0 on the left side to create the specified width.


Built-in Functions that work on String

Function	Description
len()	Python String length can be determined by using built-in len() function.
ascii()	Python ascii() function returns the string representation of the object. This function internally calls repr() function and before returning the representation string, escapes the non-ASCII characters using \x, \u or \U escapes.
bool()	Python bool() function returns Boolean value for an object. The bool class has only two instances – True and False.
bytearray()	Python bytearray() function returns a bytearray object that contains the array of bytes from the input source.
bytes()	This function returns bytes object that is an immutable sequence of integers in the range 0 <= x < 256.
ord()	Python ord() function takes string argument of a single Unicode character and return its integer Unicode code point value.
enumerate()	Python enumerate function takes a sequence, and then make each element of the sequence into a tuple.
float()	As the name says, python float() function returns a floating point number from the input argument.
hash()	This function returns the hash value of the given object.
id()	Python id() function returns the “identity” of the object. The identity of an object is an integer, which is guaranteed to be unique and constant for this object during its lifetime.
int()	Python int() function returns an integer object from the specified input. The returned int object will always be in base 10.
map()	Python map() function is used to apply a function on all the elements of specified iterable and return map object.
print()	Python print() function is used to print data into console.
slice()	Python slice() function returns a slice object representing the set of indices specified by range(start, stop, step).
type()	This function returns the type of the object.


Function Name 	Description
capitalize()	Converts the first character of the string to a capital (uppercase) letter
casefold()	Implements caseless string matching
center()	Pad the string with the specified character.
count()	Returns the number of occurrences of a substring in the string.
encode()	Encodes strings with the specified encoded scheme
endswith()	Returns "True" if a string ends with the given suffix
expandtabs()	Specifies the amount of space to be substituted with the “\t” symbol in the string
find()	Returns the lowest index of the substring if it is found
format()	Formats the string for printing it to console
format_map()	Formats specified values in a string using a dictionary
index()	Returns the position of the first occurrence of a substring in a string
isalnum()	Checks whether all the characters in a given string is alphanumeric or not
isalpha()	Returns “True” if all characters in the string are alphabets
isdecimal()	Returns true if all characters in a string are decimal
isdigit()	Returns “True” if all characters in the string are digits
isidentifier()	Check whether a string is a valid identifier or not
islower()	Checks if all characters in the string are lowercase
isnumeric()	Returns “True” if all characters in the string are numeric characters
isprintable()	Returns “True” if all characters in the string are printable or the string is empty
isspace()	Returns “True” if all characters in the string are whitespace characters
istitle()	Returns "True" if the string is a title cased string
isupper()	Checks if all characters in the string are uppercase
join()	Returns a concatenated String
ljust()	Left aligns the string according to the width specified
lower()	Converts all uppercase characters in a string into lowercase
lstrip()	Returns the string with leading characters removed
maketrans()	 Returns a translation table
partition()	Splits the string at the first occurrence of the separator
replace()	Replaces all occurrences of a substring with another substring
rfind()	Returns the highest index of the substring
rindex()	Returns the highest index of the substring inside the string
rjust()	Right aligns the string according to the width specified
rpartition()	Split the given string into three parts
rsplit()	Split the string from the right by the specified separator
rstrip()	Removes trailing characters
splitlines()	Split the lines at line boundaries
startswith()	Returns "True" if a string starts with the given prefix
strip()	Returns the string with both leading and trailing characters
swapcase()	Converts all uppercase characters to lowercase and vice versa
title()	Convert string to title case
translate()	Modify string according to given translation mappings
upper()	Converts all lowercase characters in a string into uppercase
zfill()	Returns a copy of the string with ‘0’ characters padded to the left side of the string


Examples
str.partition()
python
data = "name:John Doe:manager"

# Partition splits exactly once, returning a 3-tuple
# (before, separator, after)
left, sep, right = data.partition(':')

print(f"Left: '{left}'")
print(f"Separator: '{sep}'")
print(f"Right: '{right}'")

# Output:
# Left: 'name'
# Separator: ':'
# Right: 'John Doe:manager'
Use code with caution.

str.split()
python
data = "red-green-blue-yellow"

# Split by all occurrences of the hyphen
colors = data.split('-')

print(f"Colors: {colors}")

# Output:
# Colors: ['red', 'green', 'blue', 'yellow']
Use code with caution.

You can make split() behave more like partition() (in terms of splitting only once) by using the maxsplit=1 argument, but the return type and separator handling remain different. 
python
data = "name:John Doe:manager"

# Split only at the first occurrence (but discards the separator)
parts = data.split(':', maxsplit=1)

print(f"Parts: {parts}")
# Output:
# Parts: ['name', 'John Doe:manager']
Use code with caution.

'''

# word = 'coding'
#
# for i,c in enumerate(word):
#     print(f'''{i} - {c}''')
#
# print(f'''word.capitalize(), Converts the first character of the string to a capital (uppercase) letter \n {word.capitalize()}''')