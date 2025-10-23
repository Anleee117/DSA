def solution(arr, N, M):
    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    total = 0
    for i in range(1, N):
        if i % M == 0:
            total += arr[i]

    return total

N = int(input("Nhập số lượng phần tử N: "))
arr = list(map(int, input(f"Nhập {N} số nguyên, cách nhau bằng dấu cách: ").split()))
M = int(input("Nhập số M: "))

if N != len(arr):
    print("Số lượng phần tử không khớp với N!")
else:
    result = solution(arr, N, M)
    print("Tổng các phần tử có chỉ số bội số của M (không tính 0):", result)
