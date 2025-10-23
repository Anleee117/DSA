import math

def solution(arr, N):
    max_gcd = 0
    for pair in arr:
        a, b = pair
        gcd_value = math.gcd(a, b)
        if gcd_value > max_gcd:
            max_gcd = gcd_value
    return max_gcd


if __name__ == "__main__":
    N = int(input("Nhập số lượng cặp số N: "))
    arr = []
    print("Nhập từng cặp số, cách nhau bởi khoảng trắng:")
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append([a, b])

    result = solution(arr, N)
    print("Ước số chung lớn nhất trong các cặp là:", result)