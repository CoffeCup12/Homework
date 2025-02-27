#Shao Zhu 
#zhu.3963

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