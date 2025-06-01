import sys
import math

T = int(input())

for _ in range(T):
    N,M = map(int, input().split())
    
    answer = math.gcd(N-1, M-1) + 1
    print(answer)