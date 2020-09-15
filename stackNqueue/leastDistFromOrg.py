from queue import PriorityQueue
x = list(map(int, input().split()))
y = list(map(int, input().split()))
k = int(input())
pq = PriorityQueue()
for xi, yi in zip(x,y):
    pq.put((pow(xi,2) + pow(yi,2), (xi,yi)))
while k:
    a = pq.get()
    print(a[1], end=" ")
    k-=1