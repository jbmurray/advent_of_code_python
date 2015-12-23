import re

vowels = ['a', 'e', 'i', 'o', 'u']


def findVowels(string):
    return sum([1 for c in string if c in vowels])


def findConsecutiveChars(string):
    return re.search(r'((\D)\2+)', string)


def naughtyOrNice(string):
    strings = ['ab', 'cd', 'pq', 'xy']
    if any(substring in string for substring in strings):
        return 0
    else:
        if (findVowels(string) >= 3) & (findConsecutiveChars(string) is not None):
            return 1
        else:
            return 0


def processList(fileName):
    santasList = open(fileName)
    niceCount = 0
    for line in santasList:
        niceCount += naughtyOrNice(line.strip())
    return niceCount


if __name__ == '__main__':
    print(processList('05.txt'))
