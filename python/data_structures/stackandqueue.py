from collections import deque

print('stack-append,pop \nqueue-append,popleft')

ss = deque()

print('\nstack')
print(f'ss.append(0)')

ss.append(0)
print(f's: {ss}')
print(f'ss.append(1)')
ss.append(1)
print(f's: {ss}')
print(f'ss.append(2)')
ss.append(2)
print(f's: {ss}')
print(f'len: {len(ss)}')

print(f's: {ss}')
print(f'ss.pop()')
print(ss.pop())

print(f's: {ss}')
print(f'ss.pop()')
print(ss.pop())

print(f's: {ss}')
print(f'ss.pop()')
print(ss.pop())




print('\nqueue')
print(f'ss.append(0)')
ss.append(0)
print(f's: {ss}')

print(f'ss.append(1)')
ss.append(1)
print(f's: {ss}')

print(f'ss.append(2)')
ss.append(2)
print(f's: {ss}')
print(f'len: {len(ss)}')


print(f'ss.popleft()')
print(ss.popleft())
print(f's: {ss}')

print(f'ss.popleft()')
print(ss.popleft())
print(f's: {ss}')

print(f'ss.popleft()')
print(ss.popleft())
print(f's: {ss}')

print(f'len: {len(ss)}')
