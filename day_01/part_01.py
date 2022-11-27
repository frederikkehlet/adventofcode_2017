with open('input.txt', 'r') as file:
    numbers = file.readlines()[0]
    sum = 0
    for i in range(len(numbers) - 1):
        sum = sum + int(numbers[i]) if (numbers[i] == numbers[i+1]) else sum

    sum = sum + int(numbers[-1]) if (numbers[-1] == numbers[0]) else sum
    print(sum)
