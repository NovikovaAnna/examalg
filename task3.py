# TODO задача 2 считалочка
"Для решения задачи используем рекурсивный алгоритм:"

def last_person_standing(N, K):
    if N == 1:
        return 1
    else:
        return (last_person_standing(N-1, K) + K-1) % N + 1

# пример использования функции
N = 10
K = 3
last_person = last_person_standing(N, K)
print(f"Последний оставшийся человек имеет номер {last_person}.")