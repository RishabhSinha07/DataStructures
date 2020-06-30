def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for val in range(low, high):
        if arr[val] < pivot:
            i += 1
            arr[i], arr[val] = arr[val], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


if __name__ == "__main__":
    z = [int(x) for x in input().split()]

    quickSort(z, 0, len(z)-1)
    print(z)
