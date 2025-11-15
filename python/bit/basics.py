


print(bin(49))

print(f'''

Basic Ops - https://catonmat.net/low-level-bit-hacks

&     ->  bitwise and
|     ->  bitwise or
^     ->  bitwise xor
~     ->  bitwise not
<<    ->  bitwise shift left
>>    ->  bitwise shift right
x - 1 ->  flips right most 1 bit, and sets all the 1s to the right of it 
-x    ->  ~x+1
~x    ->  -(x+1)
    ~x  flips 0 bits to rightmost 1 bit to 0 and flips all bits on its left
    ~x + 1 ->   adding 1 to it flips rightmost bit to 1 and leaves all bits to left as is 

~x & x + 1 -> isolate right most 0
x & -x  -> isolate right most 1


play with these ops
n =       "11111111011"

#~n =     "0000100011"
#~n + 1 = "0000100100" -> -x
#~n - 1 = "0000100010"

#n - 1 =  "1111011011"

#n + 1 =  "1111011101"


1. check if n is even or odd

    n & 1 : 0 -> even, else -> odd
    print( 49 & 1)
    print( 50 & 1)
''')

print( 49 & 1)
print( 50 & 1)


print(f'''
2. Test if ith bit is set
    move 1 to nth position, do a & 0 -> not set, else is set
    x & 1 << x ? 'True' else 'False'  ''')

x1 = int("111",2)

x2 = int("11101110",2)

i = 3

if x2 & (1 << i) :
    print(True)
else:
    print(False)

print(f'''
3. Set the i-th bit.
   move 1 to nth position and do a |
    n | (1 << n) ''')

x = "11101110"
print("0b" + x)
i = 4
print(bin(int(x, 2) | 1 << i))


print(f'''
4. Unset the i-th bit.
   move 1 to i-th position, flip 0s and 1s -> do a &
    x & ~(1 << x) ''')

x = "11101110"
print("0b" + x)

i = 2
print(bin(int(x, 2) & ~(1 << i)))


print(f'''
5. Toggle the i-th bit.
   move 1 to i-th position, do a xor 
    x ^ (1 << x) ''')

x = "11101110"
print("0b" + x)

i = 2
print(bin(int(x, 2) ^ (1 << i)))

x = "11101110"
print("\n0b" + x)

i = 3
print(bin(int(x, 2) ^ (1 << i)))


print(f'''
6. Turnoff right most 1 bit.
   
    x - 1 flips right most 1 bit, and sets all the 1s to the right of it so do x & (x-1)
    x & (x-1) ''')

n = "11101000"
print("0b" + n)

x = int(n, 2)

print(f"x - 1 -> {bin(x - 1)}")
i = 2
print(bin(x & x-1))


print(f'''
7. Isolate right most 1 bit.
    

    -x  ->  ~x+1
    ~x  ->  -(x+1)
    x - 1 flips right most 1 bit, and sets all the 1s to the right of it 

    ~x  flips 0 bits to rightmost 1 bit to 0 and flips all bits on its left
    ~x + 1 ->   adding 1 to it flips rightmost bit to 1 and leaves all bits to left as is 
                and to the right as 0s  
    x & ^x + 1 or x & -x''')

n = "111100"

print("0b" + n)


x = int(n, 2)
print(f"x & (~x+1) -> {bin(x & (~x+1))}")
print(f"x & -x -> {bin(x & -x)}")



print(f'''
8. Propogate right most 1 bit.
    

    x | x - 1 ''')

n = "111100"

print("0b" + n)


x = int(n, 2)
print(f"x | x - 1 -> {bin(x | x - 1)}")


print(f'''
9. Isolate right most 0 bit.

    -x  ->  ~x+1
    ~x  ->  -(x+1)
    x - 1 flips right most 1 bit, and sets all the 1s to the right of it 

    ~x  flips 0 bits to rightmost 1 bit to 0 and flips all bits on its left
    ~x + 1 ->   adding 1 to it flips rightmost bit to 1 and leaves all bits to left as is 
                and to the right as 0s  
    ~x & x + 1 i.e x & -x ''')

n = "11110111"

print("0b" + n)


x = int(n, 2)
print(f"~ x & (x + 1) -> {bin(~x & (x + 1))}")


print(f'''
10. Turn on right most 0 bit.

    -x  ->  ~x+1
    ~x  ->  -(x+1)
    x - 1 flips right most 1 bit, and sets all the 1s to the right of it 

    ~x  flips 0 bits to rightmost 1 bit to 0 and flips all bits on its left
    ~x + 1 ->   adding 1 to it flips rightmost bit to 1 and leaves all bits to left as is 
                and to the right as 0s  
    ~x & x + 1 i.e x & -x ''')

n =       "11111111011"

#~n =     "0000100011"
#~n + 1 = "0000100100"
#~n - 1 = "0000100010"

#n - 1 =  "1111011011"

#n + 1 =  "1111011101"

print("0b" + n)


x = int(n, 2)
print(f"~ -> {bin(x | (x + 1))}")




