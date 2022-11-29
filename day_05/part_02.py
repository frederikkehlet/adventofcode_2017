with open('input.txt', 'r') as file:
    numbers = [int(line) for line in file.readlines()]
    steps, currentIndex, nextIndex = 0,0,0
    
    while currentIndex < len(numbers):
        jump = numbers[currentIndex]
        nextIndex = currentIndex + jump
        numbers[currentIndex] = numbers[currentIndex] - 1 if (jump >= 3) else numbers[currentIndex] + 1
        currentIndex = nextIndex
        steps = steps + 1

    print(steps)