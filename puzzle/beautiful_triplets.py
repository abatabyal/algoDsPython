def beautifulTriplets(d, arr):
    count = 0
    for i in range(len(arr)):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            count +=1
    return count

arr = [1, 2, 4, 5, 7, 8, 10]
d = 3
print(beautifulTriplets(d, arr))