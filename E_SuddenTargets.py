n = int(input())
times = list(map(int, input().split()))

times.sort()

C = 0
count = 0
for t in times:
    s = max(C,t)
    if s <= t + 1:
        count += 1
        C = s + 1
        
print(count)