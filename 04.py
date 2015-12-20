import hashlib


def calcHash(input):
    return hashlib.md5(input.encode('utf8')).hexdigest()


def findHash(secretKey):
    answer = 0
    while calcHash(secretKey + str(answer))[:5:] != '00000':
        answer += 1
    return str(answer)


def findHashSixZeroes(secretKey):
    answer = 0
    while calcHash(secretKey + str(answer))[:6:] != '000000':
        answer += 1
    return str(answer)


def findHashes(fileName):
    keys = open(fileName)
    print("Answer format: [SecretKey] [Answer 5 zeroes] [Answer 6 zeroes]")
    for key in keys:
        print(str(key) + " " + findHash(str(key)) + " " + findHashSixZeroes(str(key)))

if __name__ == '__main__':
    findHashes('04.txt')