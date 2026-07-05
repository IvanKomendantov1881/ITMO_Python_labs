#Сортировка пузырьком

a = [38, 27, 43, 3, 9, 82, 10, -5, 27, 0]

#Сортировка выбором
a = [38, 27, 43, 3, 9, 82, 10, -5, 27, 0]
#Класический
for i in range(len(a)):
    min_index = i
    for j in range(i+1, len(a)):
        if a[j] < a[min_index]:
            min_index = j
    a[i], a[min_index] = a[min_index], a[i]
print(a)

#Нестандартный вариант(простейший)
a_sort = []
while len(a) > 0:
    a_sort.append(min(a))
    a.remove(min(a))
print(a_sort)

#Сортировка вставками


#Сортировка слиянием
a = [38, 27, 43, 3, 9, 82, 10, -5, 27, 0]
a_new = sorted(a[0:len(a)//2])
b_new = sorted(a[len(a)//2:len(a)])


def Merge(A, B):
    i = 0
    j = 0
    res = []

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1

    res.extend(A[i:])
    res.extend(B[j:])

    return res

print(Merge(a_new, b_new))

