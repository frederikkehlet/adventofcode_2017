import re
with open('input.txt','r') as file:
    banks = [int(num) for num in (re.sub('\t',' ',file.readlines()[0])).split()]
    permutations = []
    redistributions = 0
    permutationExists = False

    while permutationExists != True:     
        blocks = max(banks)
        index = banks.index(blocks)
        banks[banks.index(blocks)] = 0 

        while blocks > 0:
            index = index + 1 if (index != len(banks) - 1) else 0
            banks[index] = banks[index] + 1
            blocks = blocks - 1

        newBanks = banks.copy()
        
        if (banks in permutations):
            permutationExists = True          
        else:
            permutations.append(newBanks)
        
        redistributions = redistributions + 1

    print(redistributions)