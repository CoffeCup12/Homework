import random

def sort(arr, start, end):

    if start < end-1:

        mid = (end + start) // 2

        sort(arr, start, mid)
        sort(arr, mid, end)

        left = arr[start:mid]
        right = arr[mid:end]

        i = 0
        j = 0
        for k in range(start, end):
            if(i < len(left) and (j == len(right) or left[i] < right[j])):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j+=1


test = [random.randint(1, 10) for num in range(10)]
print("unsorted: " + str(test))
sort(test, 0, len(test))
print("sorted: " + str(test))

test = []
print("special case: " + str(test))
sort(test, 0, len(test))
print("sorted: " + str(test))

test = [1]
print("special case2: " + str(test))
sort(test, 0, len(test))
print("sorted: " + str(test))