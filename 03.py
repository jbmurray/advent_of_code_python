import itertools

directions = {
    '<': [-1,0],
    '^': [0,1],
    '>': [1,0],
    'v': [0,-1]
}


def newLoc(lastLoc, direction):
    return [a + b for a,b in zip(lastLoc, directions[direction])]


def uniqueHouses(fileName):
    directionsList = open(fileName)
    houses = [[0,0]]
    for line in directionsList:
        for direction in line:
            houses.append(newLoc(houses[-1], direction))
    return len(set(map(tuple, houses)))



if __name__ == '__main__':
    print(uniqueHouses('03.txt'))


