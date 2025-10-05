from collections import deque

#stack
ss = deque()

ss.append(0)
ss.append(1)
ss.append(2)
print(f's: {ss}')
print(f'len: {len(ss)}')

print(ss.popleft())
print(f's: {ss}')
print(ss.popleft())
print(f's: {ss}')
print(ss.popleft())
print(f's: {ss}')

print(f'len: {len(ss)}')

print('\nqueue')
ss.append(0)
ss.append(1)
ss.append(2)
print(f'len: {len(ss)}')

print(f's: {ss}')
print(ss.pop())
print(f's: {ss}')
print(ss.pop())
print(f's: {ss}')
print(ss.pop())







