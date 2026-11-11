# Print a symmetric number pattern

n = int(input("Enter n: "))

for i in range(1, 2 * n):
    for j in range(1, 2 * n):

        if i <= n:
            row = i
        else:
            row = 2 * n - i

        if j <= n:
            col = j
        else:
            col = 2 * n - j

        if row < col:
            print(n - row + 1, end=" ")
        else:
            print(n - col + 1, end=" ")

    print()
