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


def twoSantas(fileName):
    directionsList = open(fileName)
    santa = [[0,0]]
    robot = [[0,0]]
    for line in directionsList:
        santaDirections = line[::2]
        robotDirections = line[1::2]
        for direction in santaDirections:
            santa.append(newLoc(santa[-1], direction))
        for direction in robotDirections:
            robot.append(newLoc(robot[-1], direction))
    return len(set(map(tuple, santa+robot)))


if __name__ == '__main__':
    # part 1
    print(uniqueHouses('03.txt'))
    # part 2
    print(twoSantas('03.txt'))

