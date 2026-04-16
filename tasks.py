# Задача 1: Сумма и среднее
print("=== Задача 1 ===")
values = input("Введите числа и True/False: ").split()
nums = []
for v in values:
    if v == 'True':
        nums.append(1)
    elif v == 'False':
        nums.append(0)
    else:
        nums.append(float(v))
print(f"Сумма: {sum(nums)}")
print(f"Среднее: {sum(nums)/len(nums):.6f}")

# Задача 2: Форматирование ФИО
print("\n=== Задача 2 ===")
n = int(input("Количество записей: "))
for _ in range(n):
    fio = input("ФИО: ").split()
    if len(fio) == 2:
        print(f"{fio[0]} {fio[1][0]}.")
    else:
        print(f"{fio[0]} {fio[1][0]}.{fio[2][0]}.")

# Задача 3: Разворот подстроки
print("\n=== Задача 3 ===")
s = input("Строка: ")
i, j = map(int, input("i j: ").split())
print(s[:i] + s[i:j][::-1] + s[j:])

# Задача 4: Объединение списков
print("\n=== Задача 4 ===")
a = list(map(int, input("Список 1: ").split()))
b = list(map(int, input("Список 2: ").split()))
seen = set()
res = []
for x in a + b:
    if x not in seen:
        seen.add(x)
        res.append(x)
print(res)

# Задача 5: Неубывающий фрагмент
print("\n=== Задача 5 ===")
arr = list(map(int, input("Числа: ").split()))
if not arr:
    print(0)
else:
    max_len = 1
    curr = 1
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            curr += 1
            max_len = max(max_len, curr)
        else:
            curr = 1
    print(max_len)