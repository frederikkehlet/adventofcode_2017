with open('input.txt', 'r') as file:
    rows = file.readlines()
    sum = 0

    for row in rows:
        values = [int(val) for val in row.split()]
        sum = sum + (max(values) - min(values))

    print(sum)
        