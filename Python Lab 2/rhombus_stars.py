# Print a rhombus pattern using stars

rows = int(input("Enter number of rows: "))

for i in range(rows):
    print(" " * (rows - i - 1) + "* " * rows)
