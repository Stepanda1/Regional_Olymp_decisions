import math
import sys

def main():
    data = int(input())
    if not data:
        return
    N = int(data)

    # Максимальное k такое, что k^2 <= N
    k_max = int(math.isqrt(N))
    for k in range(1, k_max + 1):
        print(k * k)

if __name__ == "__main__":
    main()
