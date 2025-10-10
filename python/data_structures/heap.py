import heapq

heap_q = []

heapq.heappush(heap_q, 3)

heapq.heappush(heap_q, 2)

heapq.heappush(heap_q, 1)


print(len(heap_q))

print(heapq.heappop(heap_q))
print(heapq.heappop(heap_q))
print(heapq.heappop(heap_q))

print(len(heap_q))

if len(heap_q)>0:
    print(heapq.heappop(heap_q))




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
