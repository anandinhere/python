import heapq


heape = []

heapq.heappush(heape,3)

heapq.heappush(heape,2)

heapq.heappush(heape,1)


print(len(heape))

print(heapq.heappop(heape))
print(heapq.heappop(heape))
print(heapq.heappop(heape))

print(len(heape))

if len(heape)>0:
    print(heapq.heappop(heape))




### min heap
import heapq

print("\n\nmin heap")
heap_l = [2,7,1,5,3]
heapq.heapify(heap_l)
while heap_l:
    print(heapq.heappop(heap_l))






print("\nmax heap")
heap_l = [2,7,1,5,3]
for x in range(len(heap_l)):
    heap_l[x]  = heap_l[x] * -1

heapq.heapify(heap_l)
while heap_l:
    print(heapq.heappop(heap_l) * -1)
