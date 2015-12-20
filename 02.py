import os


def boxSurfaceArea(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * h * l


def smallestSideArea(l, w, h):
    asc = sorted([l, w, h])
    return asc[0] * asc[1]


def wrappingPaper(l, w, h):
    return boxSurfaceArea(l, w, h) + smallestSideArea(l, w, h)


def bow(l, w, h):
    return l * w * h


def ribbon(l, w, h):
    asc = sorted([l, w, h])
    shortest1 = asc[0]
    shortest2 = asc[1]
    return shortest1 * 2 + shortest2 * 2


def calcRibbon(l, w, h):
    return bow(l, w, h) + ribbon(l, w, h)


def loopFile(fileName):
    presentList = open(fileName)
    totalPaper = 0
    totalRibbon = 0
    for present in presentList:
        dims = present.split('x')
        l, w, h = float(dims[0]), float(dims[1]), float(dims[2])
        totalPaper += wrappingPaper(l, w, h)
        totalRibbon += calcRibbon(l, w, h)
    return totalPaper, totalRibbon


if __name__ == '__main__':
    print(loopFile('02.txt'))
