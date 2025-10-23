def tim_hieu(arr, N, M):#
    window_sum = sum(arr[:M])
    max_sum = window_sum
    min_sum = window_sum
    for i in range(M, N):
        window_sum += arr[i] - arr[i - M]
        max_sum = max(max_sum, window_sum)
        min_sum = min(min_sum, window_sum)

    return max_sum - min_sum


if __name__ == "__main__":
    N, M = map(int, input("Nhập N và M: ").split())
    arr = list(map(int, input("Nhập mảng arr: ").split()))

    result = tim_hieu(arr, N, M)
    print("Kết quả :", result)