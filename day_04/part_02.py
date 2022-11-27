with open('input.txt', 'r') as file:
    passphrases = [line.strip('\n').split(' ') for line in file.readlines()]
    n_valid = 0
    
    for passphrase in passphrases:
        sortedWords = []
        for word in passphrase:          
            sortedWords.append(''.join(sorted(word)))
        
        if (len(set(sortedWords)) == len(passphrase)):
            n_valid = n_valid + 1

    print(n_valid)
            
    
        
    


        
    