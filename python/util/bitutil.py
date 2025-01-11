

def get_binary_repr(num:int):

    num_copy = num
    binary = ''
    while num != 0:

        rem = num % 2
        binary = str(rem) + binary
        num = num//2

    print(f'binary of {num_copy} : {binary}')
    return binary

def count_1s(num:int):

    mask = 1
    count = 0
    num_copy = num
    while num!=0:
        if (num ^ mask) < num:
            num = num ^ mask
            count += 1
        mask = mask << 1

    print(f'no of 1s in {num_copy} : {count}')
    return count



#print(get_binary_repr(13))