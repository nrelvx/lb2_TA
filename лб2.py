#Відлік починається з нуля
def linear_search(A, x):
    c = 0
    for i, v in enumerate(A):
        c += 1
        if v == x:
            return i, c
    return -1, c

def binary_search(A, x):
    c = 0
    l, r = 0, len(A)-1
    while l <= r:
        m = (l+r)//2
        c += 1
        if A[m] == x:
            return m, c
        c += 1
        if A[m] < x:
            l = m+1
        else:
            r = m-1
    return -1, c

def insertion_sort(A):
    c, arr = 0, A[:]
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            c +=1
            arr[j+1]=arr[j]
            j-=1
        if j>=0: c+=1
        arr[j+1]=key
    return arr, c

def quick_sort(A):
    c, arr = 0, A[:]
    def qs(l,r):
        nonlocal c
        if l<r:
            p = partition(l,r)
            qs(l,p-1)
            qs(p+1,r)
    def partition(l,r):
        nonlocal c
        pivot = arr[r]
        i = l-1
        for j in range(l,r):
            c +=1
            if arr[j]<=pivot:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[r]=arr[r],arr[i+1]
        return i+1
    qs(0,len(arr)-1)
    return arr, c

tests = [[3,7,1,9,5],[1,3,5,7,9],[2,4,6,8,10]]
search_values=[5,7,11]

print("Лінійний пошук")
for arr in tests:
    for x in search_values:
        idx,c=linear_search(arr,x)
        print(f"{arr}, x={x} -> {idx}, {c}")

print("\nДвійковий пошук")
for arr in tests:
    sarr=sorted(arr)
    for x in search_values:
        idx,c=binary_search(sarr,x)
        print(f"{sarr}, x={x} -> {idx}, {c}")

print("\nСортування вставками")
for arr in tests:
    sorted_arr,c=insertion_sort(arr)
    print(f"{arr} -> {sorted_arr}, {c}")

print("\nШвидке сортування")
for arr in tests:
    sorted_arr,c=quick_sort(arr)
    print(f"{arr} -> {sorted_arr}, {c}")
