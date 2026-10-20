def largest(arr):
    ans = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > ans:
            ans = arr[i]

    return ans