from collections import deque

def main():
    # 1) Считываем первую строку: N, K, D
    N, K, D = map(int, input().split())

    # 2) Читаем матрицу размера N×N и строим список смежности adj[1..N]
    adj = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        row = list(map(int, input().split()))
        for j in range(1, N+1):
            if row[j-1] == 1:
                adj[i].append(j)

    # 3) Читаем список из K номеров (в порядке возрастания) —
    #    это все, кто знает новость после D дней
    S = list(map(int, input().split()))
    Sset = set(S)

    possible = []
    # Проверяем кандидатов только среди тех, кто уже знает новость
    for u in S:
        dist = [-1] * (N + 1)
        dist[u] = 0
        q = deque([u])
        reached = {u}

        # BFS, но на глубину (D-1)
        while q:
            v = q.popleft()
            if dist[v] == D - 1:
                continue
            for w in adj[v]:
                if dist[w] == -1:
                    dist[w] = dist[v] + 1
                    if dist[w] <= D - 1:
                        reached.add(w)
                        q.append(w)

        # Если ровно эти K человек получат новость за D дней,
        # то dist ≤ D-1 для всех и только для всех из S
        if len(reached) == K and reached == Sset:
            possible.append(u)

    possible.sort()
    if possible:
        print(*possible)
    else:
        print()  # пустая строка, если никакого автора нет

if __name__ == "__main__":
    main()