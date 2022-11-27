with open('input.txt', 'r') as file:
    numbers = file.readlines()[0]
    sum = 0
    halfStep = int(len(numbers) / 2)

    for i in range(halfStep):
        sum = sum + int(numbers[i]) if (numbers[i] == numbers[i+halfStep]) else sum

    i = len(numbers) / 2
    for i in range(int(i),int(len(numbers))):
        sum = sum + int(numbers[i]) if (numbers[i] == numbers[abs(len(numbers) - (i + halfStep))]) else sum

    print(sum)
