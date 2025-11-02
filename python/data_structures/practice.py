
word = 'anand'


word_map = map(lambda x:str.upper(x),word)
for v in word_map:
    print(f'''{v}''')



my_tuple = (1,2,3)

print(','.join(list(map(lambda x : str(x),my_tuple))))


my_tuple = (1,2,3)

str_tuple = ' '.join(str(val) for val in my_tuple)

my_list = [1,2,3]

str_list = ' '.join(map(str, my_list))
print(str_tuple)
print(str_list)


l1 = [ 'a' , 'b' , 'c']

print( l1 + ['d'])

