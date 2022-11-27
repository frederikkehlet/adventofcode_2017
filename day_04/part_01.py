with open('input.txt', 'r') as file:
    passphrases = [line.strip('\n').split(' ') for line in file.readlines()]
    n_valid = 0
    
    n_valid = [n_valid + 1 if (len(set(passphrase)) == len(passphrase)) else n_valid for passphrase in passphrases]

    print(sum(n_valid))