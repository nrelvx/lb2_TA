# Лінійний пошук
def linear_search(arr, x):
    c = 0
    for i in range(len(arr)):        # перебираємо всі елементи
        c += 1                       # рахуємо перевірку
        if arr[i] == x:              # якщо знайшли
            return i, c
    return -1, c                     # якщо не знайшли


# Двійковий пошук (тільки для відсортованого масиву)
def binary_search(arr, x):
    c = 0
    left = 0
    right = len(arr) - 1
    while left <= right:             # поки межі не перетнулися
        mid = (left + right) // 2    # середина
        c += 1
        if arr[mid] == x:            # якщо знайшли
            return mid, c
        elif arr[mid] < x:           # шукаємо праворуч
            left = mid + 1
        else:                        # шукаємо ліворуч
            right = mid - 1
    return -1, c


# Сортування вставками
def insertion_sort(arr):
    c = 0
    for i in range(1, len(arr)):     # починаємо з другого елемента
        key = arr[i]                 # елемент який вставляємо
        j = i - 1
        while j >= 0 and arr[j] > key:
            c += 1
            arr[j+1] = arr[j]        # зсув праворуч
            j -= 1
        if j >= 0:                   # якщо while не зайшов
            c += 1
        arr[j+1] = key               # вставка key
    return arr, c


# Швидке сортування 
def quick_sort(arr):
    c = 0

    if len(arr) <= 1:
        return arr, c

    pivot = arr[0]                   # опорний елемент (перший)
    left = []
    right = []
    for i in range(1, len(arr)):
        c += 1
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    lsorted, c1 = quick_sort(left)   # рекурсія для лівої частини
    rsorted, c2 = quick_sort(right)  # рекурсія для правої частини

    return lsorted + [pivot] + rsorted, c + c1 + c2

tests = [[3, 7, 1, 9, 5], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]
search_values = [5, 7, 11]

print("Лінійний пошук")
for arr in tests:
    for x in search_values:
        idx, c = linear_search(arr, x)
        print(arr, "x=", x, "-> idx=", idx, "порівнянь=", c)

print("\nДвійковий пошук")
for arr in tests:
    sarr = sorted(arr)
    for x in search_values:
        idx, c = binary_search(sarr, x)
        print(sarr, "x=", x, "-> idx=", idx, "порівнянь=", c)

print("\nСортування вставками")
for arr in tests:
    sorted_arr, c = insertion_sort(arr[:])  # [:] щоб не псувати оригінал
    print(arr, "->", sorted_arr, "порівнянь=", c)

print("\nШвидке сортування")
for arr in tests:
    sorted_arr, c = quick_sort(arr[:])
    print(arr, "->", sorted_arr, "порівнянь=", c)
