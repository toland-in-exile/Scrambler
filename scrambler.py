import random
import sys

lineNum = 0

fileIn = open(f'{sys.argv[1]}', 'r')

for line in fileIn:
    strIn = line
    userIn = strIn.split()
    keyList = userIn.copy()
    encrypted = []
    key = []
    while len(userIn) != 0:
        remDex = random.randint(0, len(userIn) - 1)
        remWord = userIn.pop(remDex)
        encrypted.append(remWord)
        key.append(keyList.index(remWord))
    with open('Error - encrypted.txt', 'a') as scramFile:
        scramFile.write(' '.join(map(str, encrypted)))
        scramFile.write('\n')
    with open('Birthdays.txt', 'a') as keyFile:
        keyFile.write((' '.join(map(str, key))))
        keyFile.write('\n')
    print(f'line processed: {lineNum}')
    lineNum += 1


fileIn.close()
scramFile.close()
keyFile.close()


