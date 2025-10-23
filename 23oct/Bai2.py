def watering_can(watering_can, N, M):
    garden = [[0] * N for _ in range(N)]

    for can in watering_can:
        r, c, power = can
        garden[r][c] = 1

        for k in range(1, power + 1):
            if r - k >= 0:
                garden[r - k][c] = 1
            if r + k < N:
                garden[r + k][c] = 1
            if c - k >= 0:
                garden[r][c - k] = 1
            if c + k < N:
                garden[r][c + k] = 1

    dry_cells = sum(row.count(0) for row in garden)
    return dry_cells

if __name__ == "__main__":
    N, M = map(int, input("Nhập N và M: ").split())

    watering_can_list = []
    print(f"Nhập thông tin {M} vòi phun (hàng, cột, cường độ):")
    for i in range(M):
        r, c, power = map(int, input(f"Vòi {i+1}: ").split())
        watering_can_list.append([r, c, power])

    result = watering_can(watering_can_list, N, M)

    print("Số ô không được tưới:", result)
