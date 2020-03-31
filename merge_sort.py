def mergesort(arr):

    if len(arr)>1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        x = y = z = 0

        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                arr[z] = left[x]
                x = x+1
            else:
                arr[z] = right[y]
                y = y+1
            z = z+1

        while(x < len(left)):
            arr[z] = left[x]
            z = z+1
            x = x+1
        while (y < len(right)):
            arr[z] = right[y]
            z = z + 1
            y = y + 1

    return arr

if __name__ == '__main__':
    ar = [10,9,8,7,6,5,4,3,3,2,1,1001,1002,999]
    print(mergesort(ar))



