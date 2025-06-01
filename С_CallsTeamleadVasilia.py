from bisect import bisect_left

def main():
    # Читаем все числа из одной строки
    data = list(map(int, input().split()))
    
    # Первое число — N, далее идут 3*N чисел (s, e, p)
    n = data[0]
    triples = []
    idx = 1
    for _ in range(n):
        s = data[idx]
        e = data[idx+1]
        p = data[idx+2]
        idx += 3
        triples.append((s, e, p))
    
    # Сортируем звонки по убыванию приоритета
    triples.sort(key=lambda x: -x[2])
    
    accepted = []  # список принятых (непересекающихся) интервалов (s, e), отсортирован по s
    skipped_sum = 0
    
    for s, e, p in triples:
        # Найдём позицию i, куда вставить (s, e) по ключу s
        i = bisect_left(accepted, (s, e))
        conflict = False
        
        # Проверяем пересечение с предыдущим интервалом (если i > 0)
        if i > 0:
            s0, e0 = accepted[i - 1]
            if s < e0:
                conflict = True
        
        # Проверяем пересечение с «текущим» интервалом в accepted[i] (если i < len)
        if not conflict and i < len(accepted):
            s1, e1 = accepted[i]
            if e > s1:
                conflict = True
        
        if conflict:
            skipped_sum += p
        else:
            accepted.insert(i, (s, e))
    
    print(skipped_sum)

if __name__ == "__main__":
    main()