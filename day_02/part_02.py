with open('input.txt', 'r') as file:
    rows = file.readlines()
    sum = 0

    for row in rows:
        values = [int(val) for val in row.split()]
        
        currentIndex = 0
        while currentIndex < len(values):
            for i in range(currentIndex,len(values) - 1):
                if (values[currentIndex] % values[i] == 0):
                    sum = sum + (values[currentIndex] / values[i])
            currentIndex += 1
            

    print(int(sum))