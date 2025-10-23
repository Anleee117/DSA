def nhan_keo(arr, N, J):
    total = sum(arr)
    
    if total != 0:
        J = J % total  

    if J == 0:
        return N

    for i in range(N):
        J -= arr[i]
        if J <= 0:
            return i + 1



if __name__ == "__main__":
    N, J = map(int, input("Nhập N và J: ").split())
    arr = list(map(int, input("Nhập danh sách kẹo mỗi em muốn nhận: ").split()))

    result = nhan_keo(arr, N, J)
    print("Em nhỏ cuối cùng nhận được kẹo là em số:", result)