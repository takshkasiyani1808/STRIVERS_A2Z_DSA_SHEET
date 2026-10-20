def print2largest(arr):
    prev = -1
    curr = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > curr:
            prev = curr
            curr = arr[i]
        elif arr[i] > prev and arr[i] != curr:
            prev = arr[i]
    return prev
