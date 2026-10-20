def largest(arr):
    ans = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > ans:
            ans = arr[i]

    return ans

print(largest([0,3,24,52,351,3,13]))