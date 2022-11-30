import operator

ops = { 
    ">": operator.gt, 
    "<": operator.lt, 
    ">=": operator.ge, 
    "<=": operator.le, 
    "==": operator.eq, 
    "!=": operator.ne,
    "dec": operator.sub,
    "inc": operator.add
}

with open('input.txt', 'r') as file:
    lines = file.readlines()
    registers = {k:v for x in [{register: 0 } for register in list(set([line.split(' ')[0] for line in lines]))] for k,v in x.items()} 
    register_history =  registers.copy()   
    
    for line in lines:
        operation = [line.strip() for line in line.split(' if ')[0].split(' ')]
        condition = [line.strip() for line in line.split(' if ')[1].split(' ')]

        if (ops[condition[1]](int(registers.get(condition[0])),int(condition[2]))):
            registers[operation[0]] = registers[operation[0]] + int(operation[2]) if operation[1] == "inc" else registers[operation[0]] - int(operation[2])
            
            if (registers[operation[0]] > register_history[operation[0]]):
                register_history[operation[0]] = registers[operation[0]]
        
    print(list(sorted(register_history.items(), key=lambda x:x[1])[-1])[1])