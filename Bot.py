import random
import math

data = None
WEIGHTS = [[0, 0.1, 0.1], [0, 0.1, 0.25], [0, 2, 5], [0, 4, 7], [0, 6, 100], [200, 200, 200]]


class Attack:
    def __init__(self, len=0, pot=0, div=1):
        self.length = len
        self.potential = pot
        self.divider = div

    def countWeigth(self):
        return WEIGHTS[self.length][self.potential] / self.divider


class CheckLine:
    def __init__(self):
        self.subFig = 1
        self.Attacks = []
        self.curAttack = Attack()
        self.iter = 1
        self.checkEdge = False
        self.attack_place = 1


    def getAttacks(self, cellX, cellY, subFig, dx, dy):
        self.substitudeFigure(subFig)
        x = cellX - dx
        y = cellY - dy

        while abs(x - cellX) <= 5 and abs(y - cellY) <= 5:
            if self.checkCell(x, y):
                break
            x -= dx
            y -= dy

        self.turnAround()

        x = cellX + dx
        y = cellY + dy

        while abs(x - cellX) <= 5 and abs(y - cellY) <= 5:
            if self.checkCell(x, y):
                break
            x += dx
            y += dy

        return self.Attacks

    def checkCell(self, x, y):
        fig = data[x][y] if data[x] and data[x][y] != 0 else 'b'

        if self.iter == 4 and fig == self.subFig:
            self.checkEdge = True
        elif self.iter == 5:
            self.checkEdgeCell(x, y)
            return 0
        self.iter += 1

        if fig == -1 or fig == 1:
            if self.subFig != fig:
                self.Attacks.append(self.curAttack)
                return fig
            else:
                self.curAttack.length += 1
                self.attack_place += 1
        elif fig == 'b':
            self.Attacks.append(self.curAttack)
            return 'b'

        else:
            if self.curAttack.length:
                self.curAttack.potential += 1
                self.Attacks.append(self.curAttack)
                self.curAttack = Attack()
                self.curAttack.potential += 1
            self.curAttack.divider += 1
            self.attack_place += 1


    def substitudeFigure(self, fig):
        self.subFig = fig
        self.curAttack.length += 1

    def checkEdgeCell(self, x, y):
        if self.checkEdge:
            fig = data[x][y] if data[x] and data[x][y] != 0 else 'b'
            if fig == self.subFig or fig == 0:
                self.curAttack.potential += 1
            if self.curAttack.length:
                self.Attacks.append(self.curAttack)

    def turnAround(self):
        self.iter = 1
        self.checkEdge = False
        self.curAttack = self.Attacks[0]
        self.Attacks.pop()


def countWeight(x, y):
    def count(atks, curFig):
        weight = 0
        breakPoints = 0

        for p in ['0', '45', '90', '135']:
            if isBreakPoint(atks[p]):
                breakPoints += 1
                if breakPoints == 2:
                    weight += 100
                    return
            for a in atks[p]:
                if a.length > 5:
                    a.length = 5
                if a.length == 5 and curFig == -1:
                    weight += 100
                weight += WEIGHTS[a.length][a.potential] / a.divider
        return weight

    attacks = getAllAttacks(x, y)
    if not attacks:
        return
    sum = 0
    sum += count(attacks[1], 1)
    sum += count(attacks[-1], -1)
    return sum


def getAllAttacks(cellX, cellY):
    if data[cellX][cellY]:
        return False

    cX = {}
    cO = {}

    cX['0'] = getAttacksLine(cellX, cellY, 1, 1, 0)
    cX['90'] = getAttacksLine(cellX, cellY, 1, 0, 1)
    cX['45'] = getAttacksLine(cellX, cellY, 1, 1, -1)
    cX['135'] = getAttacksLine(cellX, cellY, 1, 1, 1)

    cO['0'] = getAttacksLine(cellX, cellY, -1, 1, 0)
    cO['90'] = getAttacksLine(cellX, cellY, -1, 0, 1)
    cO['45'] = getAttacksLine(cellX, cellY, -1, 1, -1)
    cO['135'] = getAttacksLine(cellX, cellY, -1, 1, 1)

    return {
        1: cX,
        -1: cO
    }


def getAttacksLine(cellX, cellY, subFig, dx, dy):
    C = CheckLine()
    C.getAttacks(cellX, cellY, subFig, dx, dy)
    return filterAttacks(C)


def filterAttacks(attackLine):
    res = []
    if attackLine.attack_place >= 5:
        for i in attackLine.Attacks:
            if i.length and i.potential or i.length >= 5:
                res.append(i)
    attackLine.Attacks = res
    return res


def isBreakPoint(attackLine):
    if not attackLine or not len(attackLine):
        return False
    centAtk = 0

    for a in attackLine:
        if a.divider == 1:
            centAtk = a

    if centAtk.length >= 4:
        return True
    if centAtk.potential == 2 and centAtk.length >= 3:
        return True

    res = False

    for a in attackLine:
        score = centAtk.length
        if a.divider == 2:
            if centAtk.potential == 2 and a.potential == 2:
                score += 1
            if score + a.length >= 4:
                res = True
                return
    return res


def bot(_data):
    global data
    data = _data
    max = 0
    best_x = random.randint(10,29)
    best_y = random.randint(10,29)
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                try:
                    if max < countWeight(i, j):
                        max = countWeight(i, j)
                        best_x = i
                        best_y = j
                except TypeError:
                    continue
    print(data)
    print(best_x, best_y)
    return (best_x, best_y)

