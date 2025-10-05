from functools import reduce

l = [i for i in range(10)]
print(l)

f = filter(lambda x:x==0,l) #returns iterator
print(list(f))

m = map(lambda x:x/2,l) #returns iterator
print(list(m))

r = reduce(lambda x,y:x+y,l)
print(r)



s = 'ab1njds4kkj233khds1'

n = filter(lambda x: str.isdigit(x),list(s))
number = ''.join(sorted(list(n)))
print(int(number))