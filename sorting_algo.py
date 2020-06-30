def bubbleSort(arr,l):
    for i in range(l):
        for j in range(l-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def selectionSort(arr, l):
    for x in range(l-1):
        temp = -1
        for y in range(x+1, l):
            if arr[y] < arr[x]:
                temp = y
        if temp != -1:
            arr[x],arr[temp] = arr[temp],arr[x]
    return arr

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    l = len(arr)
    z = selectionSort(arr,l)
    print(' '.join(list(map(str,z))))