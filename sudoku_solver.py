import time

def checkExistingValues_ROW(row):
    i = 0
    numArray = []
    while i < 9:
        if row[i] != '-':
            numArray.append(row[i])
        i = i + 1
    return numArray

def checkExistingValues_COL(myGrid, colNum):
    i = 0
    numArray = []
    while i < 9:
        if myGrid[i][colNum] != '-':
            numArray.append(myGrid[i][colNum])
        i = i + 1
    return numArray

#Checks the values of one small 9-box-grid. Pass in which grid 0-8
def checkExistingValuesSmallGrid(myGrid, gridToCheck):
    returnThisDictionary = []
    if gridToCheck == 0:
        i = 0
        j = 0
        while i < 3:
            while j < 3:
                if myGrid[i][j] != '-':
                    returnThisDictionary.extend(myGrid[i][j])
                j = j + 1
            i = i + 1
            j = 0
        return returnThisDictionary
    if gridToCheck == 1:
        i = 0
        j = 3
        while i < 3:
            while j < 6:
                if myGrid[i][j] != '-':
                    returnThisDictionary.extend(myGrid[i][j])
                j = j + 1
            i = i + 1
            j = 3
        return returnThisDictionary
    if gridToCheck == 2:
        i = 0
        j = 6
        while i < 3:
            while j < 9:
                if myGrid[i][j] != '-':
                    returnThisDictionary.extend(myGrid[i][j])
                j = j + 1
            i = i + 1
            j = 6
        return returnThisDictionary
    if gridToCheck == 3:
        i = 3
        j = 0
        while i < 6:
            while j < 3:
                if myGrid[i][j] != '-':
                    returnThisDictionary.extend(myGrid[i][j])
                j = j + 1
            i = i + 1
            j = 0
        return returnThisDictionary
    if gridToCheck == 4:
        i = 3
        j = 3
        while i < 6:
            while j < 6:
                if myGrid[i][j] != '-':
                    returnThisDictionary.extend(myGrid[i][j])
                j = j + 1
            i = i + 1
            j = 3
        return returnThisDictionary
    if gridToCheck == 5:
        i = 3
        j = 6
        while i < 6:
            while j < 9:
                if myGrid[i][j] != '-':
                    returnThisDictionary.extend(myGrid[i][j])
                j = j + 1
            i = i + 1
            j = 6
        return returnThisDictionary
    if gridToCheck == 6:
        i = 6
        j = 0
        while i < 9:
            while j < 3:
                if myGrid[i][j] != '-':
                    returnThisDictionary.extend(myGrid[i][j])
                j = j + 1
            i = i + 1
            j = 0
        return returnThisDictionary
    if gridToCheck == 7:
        i = 6
        j = 3
        while i < 9:
            while j < 6:
                if myGrid[i][j] != '-':
                    returnThisDictionary.extend(myGrid[i][j])
                j = j + 1
            i = i + 1
            j = 3
        return returnThisDictionary
    if gridToCheck == 8:
        i = 6
        j = 6
        while i < 9:
            while j < 9:
                if myGrid[i][j] != '-':
                    returnThisDictionary.extend(myGrid[i][j])
                j = j + 1
            i = i + 1
            j = 6
        return returnThisDictionary


def checkExistingValues_SMALL_SQ(row1, row2, row3):
    i = 0
    n = 0
    m = 0
    numArray = []
    while i < 4:
        if row1[i] != '-':
            numArray.extend(row1[i])
        i = i + 1
    while n < 4:
        if row2[n] != '-':
            numArray.extend(row2[n])
        n = n + 1
    while m < 4:
        if row3[m] != '-':
            numArray.extend(row3[m])
        m = m + 1
    return numArray

def makeColumn(row1, row2, row3, row4, row5, row6, row7, row8, row9, returnedColumn):
    column = [row1[returnedColumn], row2[returnedColumn], row3[returnedColumn], row4[returnedColumn], row5[returnedColumn], row6[returnedColumn], row7[returnedColumn], row8[returnedColumn], row9[returnedColumn]]
    return column

def removeDuplicates(myList):
    # using naive method
    # to remove duplicated
    # from list
    res = []
    for i in myList:
        if i not in res:
            res.append(i)
    return res

def takeThreeRemoveDuplicate(set1, set2, set3):
    container = []
    container.extend(set1)
    container.extend(set2)
    container.extend(set3)
    return removeDuplicates(container)

def printGrid(myGrid):
    i = 0
    j = 0
    line = []
    while j < 9:
        while i < 9:
            line.append(myGrid[j][i])
            if i == 8:
                print(line)
            i = i + 1
        j = j + 1
        i = 0
        line = []

def tallyPossibleValuesFullGrid(myGrid):
    holdPossibleValues = []
    coordinateBasedNegative = []

    oneToTen = ['1','2','3','4','5','6','7','8','9']
    #R = Row, C = Column, M = mini square
    R = 0
    C = 0
    M = 0
    countItems = 0
    ott = 0

    f = open("Tally_Values.txt", "w")


    # Mini-square 1 , row 0 - 2 , column 0 - 2
    #While mini square is M
    while M < 1:
        #While row is R
        while R < 3:
            #while column is C
            while C < 3:
                #Find what values cannot be used at this coordinate
                coordinateBasedNegative.append(takeThreeRemoveDuplicate(checkExistingValues_ROW(myGrid[R]), checkExistingValues_COL(myGrid, C), checkExistingValuesSmallGrid(myGrid, M)))
                #print(coordinateBasedNegative)
                #For each value that already exists, mark oneToTen by removing that value from list
                while countItems < coordinateBasedNegative[0].__len__():
                    while ott < 9:
                        if oneToTen[ott] == coordinateBasedNegative[0][countItems]:
                            #print(oneToTen[ott])
                            #print(coordinateBasedNegative[0][countItems])
                            oneToTen[ott] = '-'
                            #print(oneToTen[ott])
                        ott = ott + 1
                    #print(oneToTen)
                    countItems = countItems + 1
                    ott = 0
                print("final count: R=" + str(R) + "C=" + str(C))
                f.write("final count: R=" + str(R) + "C=" + str(C) + "\n")
                C = C + 1
                print(oneToTen)
                f.write(str(oneToTen) + '\n')
                oneToTen.append(R)
                oneToTen.append(C)
                oneToTen.append(M)
                holdPossibleValues.append(oneToTen)
                countItems = 0
                coordinateBasedNegative = []
                oneToTen = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            R = R + 1
            C = 0
        M = M + 1
        R = 0



    oneToTen = ['1','2','3','4','5','6','7','8','9']
    #R = Row, C = Column, M = mini square
    R = 0
    C = 3
    M = 1
    countItems = 0
    ott = 0

    # Mini-square 1 , row 0 - 2 , column 0 - 2
    #While mini square is M
    while M < 2:
        #While row is R
        while R < 3:
            #while column is C
            while C < 6:
                #Find what values cannot be used at this coordinate
                coordinateBasedNegative.append(takeThreeRemoveDuplicate(checkExistingValues_ROW(myGrid[R]), checkExistingValues_COL(myGrid, C), checkExistingValuesSmallGrid(myGrid, M)))
                #print(coordinateBasedNegative)
                #For each value that already exists, mark oneToTen by removing that value from list
                while countItems < coordinateBasedNegative[0].__len__():
                    while ott < 9:
                        if oneToTen[ott] == coordinateBasedNegative[0][countItems]:
                            #print(oneToTen[ott])
                            #print(coordinateBasedNegative[0][countItems])
                            oneToTen[ott] = '-'
                            #print(oneToTen[ott])
                        ott = ott + 1
                    #print(oneToTen)
                    countItems = countItems + 1
                    ott = 0
                print("final count: R=" + str(R) + "C=" + str(C))
                f.write("final count: R=" + str(R) + "C=" + str(C) + "\n")
                C = C + 1
                print(oneToTen)
                f.write(str(oneToTen) + '\n')
                oneToTen.append(R)
                oneToTen.append(C)
                oneToTen.append(M)
                holdPossibleValues.append(oneToTen)
                countItems = 0
                coordinateBasedNegative = []
                oneToTen = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            R = R + 1
            C = 3
        M = M + 1
        R = 0



    oneToTen = ['1','2','3','4','5','6','7','8','9']
    #R = Row, C = Column, M = mini square
    R = 0
    C = 6
    M = 2
    countItems = 0
    ott = 0

    # Mini-square 1 , row 0 - 2 , column 0 - 2
    #While mini square is M
    while M < 3:
        #While row is R
        while R < 3:
            #while column is C
            while C < 9:
                #Find what values cannot be used at this coordinate
                coordinateBasedNegative.append(takeThreeRemoveDuplicate(checkExistingValues_ROW(myGrid[R]), checkExistingValues_COL(myGrid, C), checkExistingValuesSmallGrid(myGrid, M)))
                #print(coordinateBasedNegative)
                #For each value that already exists, mark oneToTen by removing that value from list
                while countItems < coordinateBasedNegative[0].__len__():
                    while ott < 9:
                        if oneToTen[ott] == coordinateBasedNegative[0][countItems]:
                            #print(oneToTen[ott])
                            #print(coordinateBasedNegative[0][countItems])
                            oneToTen[ott] = '-'
                            #print(oneToTen[ott])
                        ott = ott + 1
                    #print(oneToTen)
                    countItems = countItems + 1
                    ott = 0
                print("final count: R=" + str(R) + "C=" + str(C))
                f.write("final count: R=" + str(R) + "C=" + str(C) + "\n")
                C = C + 1
                print(oneToTen)
                f.write(str(oneToTen) + '\n')
                oneToTen.append(R)
                oneToTen.append(C)
                oneToTen.append(M)
                holdPossibleValues.append(oneToTen)
                countItems = 0
                coordinateBasedNegative = []
                oneToTen = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            R = R + 1
            C = 6
        M = M + 1
        R = 0



    oneToTen = ['1','2','3','4','5','6','7','8','9']
    #R = Row, C = Column, M = mini square
    R = 3
    C = 0
    M = 3
    countItems = 0
    ott = 0

    # Mini-square 1 , row 0 - 2 , column 0 - 2
    #While mini square is M
    while M < 4:
        #While row is R
        while R < 6:
            #while column is C
            while C < 3:
                #Find what values cannot be used at this coordinate
                coordinateBasedNegative.append(takeThreeRemoveDuplicate(checkExistingValues_ROW(myGrid[R]), checkExistingValues_COL(myGrid, C), checkExistingValuesSmallGrid(myGrid, M)))
                #print(coordinateBasedNegative)
                #For each value that already exists, mark oneToTen by removing that value from list
                while countItems < coordinateBasedNegative[0].__len__():
                    while ott < 9:
                        if oneToTen[ott] == coordinateBasedNegative[0][countItems]:
                            #print(oneToTen[ott])
                            #print(coordinateBasedNegative[0][countItems])
                            oneToTen[ott] = '-'
                            #print(oneToTen[ott])
                        ott = ott + 1
                    #print(oneToTen)
                    countItems = countItems + 1
                    ott = 0
                print("final count: R=" + str(R) + "C=" + str(C))
                f.write("final count: R=" + str(R) + "C=" + str(C) + "\n")
                C = C + 1
                print(oneToTen)
                f.write(str(oneToTen) + '\n')
                oneToTen.append(R)
                oneToTen.append(C)
                oneToTen.append(M)
                holdPossibleValues.append(oneToTen)
                countItems = 0
                coordinateBasedNegative = []
                oneToTen = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            R = R + 1
            C = 0
        M = M + 1
        R = 3

    oneToTen = ['1','2','3','4','5','6','7','8','9']
    #R = Row, C = Column, M = mini square
    R = 3
    C = 3
    M = 4
    countItems = 0
    ott = 0

    # Mini-square 2 , row 0 - 2 , column 3 - 5
    #While mini square is M
    while M < 5:
        #While row is R
        while R < 6:
            #while column is C
            while C < 6:
                #Find what values cannot be used at this coordinate
                coordinateBasedNegative.append(takeThreeRemoveDuplicate(checkExistingValues_ROW(myGrid[R]), checkExistingValues_COL(myGrid, C), checkExistingValuesSmallGrid(myGrid, M)))
                #print(coordinateBasedNegative)
                #For each value that already exists, mark oneToTen by removing that value from list
                while countItems < coordinateBasedNegative[0].__len__():
                    while ott < 9:
                        if oneToTen[ott] == coordinateBasedNegative[0][countItems]:
                            #print(oneToTen[ott])
                            #print(coordinateBasedNegative[0][countItems])
                            oneToTen[ott] = '-'
                            #print(oneToTen[ott])
                        ott = ott + 1
                    #print(oneToTen)
                    countItems = countItems + 1
                    ott = 0
                print("final count: R=" + str(R) + "C=" + str(C))
                f.write("final count: R=" + str(R) + "C=" + str(C) + "\n")
                C = C + 1
                print(oneToTen)
                f.write(str(oneToTen) + '\n')
                oneToTen.append(R)
                oneToTen.append(C)
                oneToTen.append(M)
                holdPossibleValues.append(oneToTen)
                countItems = 0
                coordinateBasedNegative = []
                oneToTen = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            R = R + 1
            C = 3
        M = M + 1
        R = 3

    #Mini-square 3 , row 0 - 2 , column 6 - 8
    oneToTen = ['1','2','3','4','5','6','7','8','9']
    #R = Row, C = Column, M = mini square
    R = 3
    C = 6
    M = 5
    countItems = 0
    ott = 0

    #While mini square is M
    while M < 6:
        #While row is R
        while R < 6:
            #while column is C
            while C < 9:
                #Find what values cannot be used at this coordinate
                coordinateBasedNegative.append(takeThreeRemoveDuplicate(checkExistingValues_ROW(myGrid[R]), checkExistingValues_COL(myGrid, C), checkExistingValuesSmallGrid(myGrid, M)))
                #print(coordinateBasedNegative)
                #For each value that already exists, mark oneToTen by removing that value from list
                while countItems < coordinateBasedNegative[0].__len__():
                    while ott < 9:
                        if oneToTen[ott] == coordinateBasedNegative[0][countItems]:
                            #print(oneToTen[ott])
                            #print(coordinateBasedNegative[0][countItems])
                            oneToTen[ott] = '-'
                            #print(oneToTen[ott])
                        ott = ott + 1
                    #print(oneToTen)
                    countItems = countItems + 1
                    ott = 0
                print("final count: R=" + str(R) + "C=" + str(C))
                f.write("final count: R=" + str(R) + "C=" + str(C) + "\n")
                C = C + 1
                print(oneToTen)
                f.write(str(oneToTen) + '\n')
                oneToTen.append(R)
                oneToTen.append(C)
                oneToTen.append(M)
                holdPossibleValues.append(oneToTen)
                countItems = 0
                coordinateBasedNegative = []
                oneToTen = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            R = R + 1
            C = 6
        M = M + 1
        R = 3

    oneToTen = ['1','2','3','4','5','6','7','8','9']
    #R = Row, C = Column, M = mini square
    R = 6
    C = 0
    M = 6
    countItems = 0
    ott = 0

    # Mini-square 1 , row 0 - 2 , column 0 - 2
    #While mini square is M
    while M < 7:
        #While row is R
        while R < 9:
            #while column is C
            while C < 3:
                #Find what values cannot be used at this coordinate
                coordinateBasedNegative.append(takeThreeRemoveDuplicate(checkExistingValues_ROW(myGrid[R]), checkExistingValues_COL(myGrid, C), checkExistingValuesSmallGrid(myGrid, M)))
                #print(coordinateBasedNegative)
                #For each value that already exists, mark oneToTen by removing that value from list
                while countItems < coordinateBasedNegative[0].__len__():
                    while ott < 9:
                        if oneToTen[ott] == coordinateBasedNegative[0][countItems]:
                            #print(oneToTen[ott])
                            #print(coordinateBasedNegative[0][countItems])
                            oneToTen[ott] = '-'
                            #print(oneToTen[ott])
                        ott = ott + 1
                    #print(oneToTen)
                    countItems = countItems + 1
                    ott = 0
                print("final count: R=" + str(R) + "C=" + str(C))
                f.write("final count: R=" + str(R) + "C=" + str(C) + "\n")
                C = C + 1
                print(oneToTen)
                f.write(str(oneToTen) + '\n')
                oneToTen.append(R)
                oneToTen.append(C)
                oneToTen.append(M)
                holdPossibleValues.append(oneToTen)
                countItems = 0
                coordinateBasedNegative = []
                oneToTen = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            R = R + 1
            C = 0
        M = M + 1
        R = 6

    oneToTen = ['1','2','3','4','5','6','7','8','9']
    #R = Row, C = Column, M = mini square
    R = 6
    C = 3
    M = 7
    countItems = 0
    ott = 0

    # Mini-square 2 , row 0 - 2 , column 3 - 5
    #While mini square is M
    while M < 8:
        #While row is R
        while R < 9:
            #while column is C
            while C < 6:
                #Find what values cannot be used at this coordinate
                coordinateBasedNegative.append(takeThreeRemoveDuplicate(checkExistingValues_ROW(myGrid[R]), checkExistingValues_COL(myGrid, C), checkExistingValuesSmallGrid(myGrid, M)))
                #print(coordinateBasedNegative)
                #For each value that already exists, mark oneToTen by removing that value from list
                while countItems < coordinateBasedNegative[0].__len__():
                    while ott < 9:
                        if oneToTen[ott] == coordinateBasedNegative[0][countItems]:
                            #print(oneToTen[ott])
                            #print(coordinateBasedNegative[0][countItems])
                            oneToTen[ott] = '-'
                            #print(oneToTen[ott])
                        ott = ott + 1
                    #print(oneToTen)
                    countItems = countItems + 1
                    ott = 0
                print("final count: R=" + str(R) + "C=" + str(C))
                f.write("final count: R=" + str(R) + "C=" + str(C) + "\n")
                C = C + 1
                print(oneToTen)
                f.write(str(oneToTen) + '\n')
                oneToTen.append(R)
                oneToTen.append(C)
                oneToTen.append(M)
                holdPossibleValues.append(oneToTen)
                countItems = 0
                coordinateBasedNegative = []
                oneToTen = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            R = R + 1
            C = 3
        M = M + 1
        R = 6

    #Mini-square 3 , row 0 - 2 , column 6 - 8
    oneToTen = ['1','2','3','4','5','6','7','8','9']
    #R = Row, C = Column, M = mini square
    R = 6
    C = 6
    M = 8
    countItems = 0
    ott = 0

    #While mini square is M
    while M < 9:
        #While row is R
        while R < 9:
            #while column is C
            while C < 9:
                #Find what values cannot be used at this coordinate
                coordinateBasedNegative.append(takeThreeRemoveDuplicate(checkExistingValues_ROW(myGrid[R]), checkExistingValues_COL(myGrid, C), checkExistingValuesSmallGrid(myGrid, M)))
                #print(coordinateBasedNegative)
                #For each value that already exists, mark oneToTen by removing that value from list
                while countItems < coordinateBasedNegative[0].__len__():
                    while ott < 9:
                        if oneToTen[ott] == coordinateBasedNegative[0][countItems]:
                            #print(oneToTen[ott])
                            #print(coordinateBasedNegative[0][countItems])
                            oneToTen[ott] = '-'
                            #print(oneToTen[ott])
                        ott = ott + 1
                    #print(oneToTen)
                    countItems = countItems + 1
                    ott = 0
                print("final count: R=" + str(R) + "C=" + str(C))
                f.write("final count: R=" + str(R) + "C=" + str(C) + "\n")
                C = C + 1
                print(oneToTen)
                f.write(str(oneToTen) + '\n')
                oneToTen.append(R)
                oneToTen.append(C)
                oneToTen.append(M)
                holdPossibleValues.append(oneToTen)
                countItems = 0
                coordinateBasedNegative = []
                oneToTen = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            R = R + 1
            C = 6
        M = M + 1
        R = 6
    f.close()
    return holdPossibleValues



def makeNewGrid(myGrid, row, col, val):
    i = 0
    j = 0
    newGrid = []
    newLine = []
    while i < row:
        newGrid.append(myGrid[0][i])
        #print(myGrid[0][i])
        i = i + 1

    print("I'm about to replace a number...")
    while j <= 9:
        if j == col:
            newLine.extend(val)
            print("I just swapped something for " + val + "position:" + str(row) + str(col))
        if j != col:
            newLine.extend(myGrid[0][i][j])
        j = j + 1
    3#newLine.extend('\n')
    #print(newLine)
    #print(newLine[0])
    pleaseWork = newLine[0] + newLine[1] + newLine[2] + newLine[3] + newLine[4] + newLine[5] + newLine[6] + newLine[7] + newLine[8] + '\n'
    print(pleaseWork)
    newGrid.append(pleaseWork)
    i = i + 1

    while i < 9:
        newGrid.append(myGrid[0][i])
        i = i + 1
    print(newGrid)
    #time.sleep(.5)

    return newGrid





#f=open("board.txt", "r")
#f=open("newboard.txt", "r")
f=open('EditThisFile.txt', "r")
if f.mode == 'r':
    lineA = f.readline()
    lineB = f.readline()
    lineC = f.readline()
    lineD = f.readline()
    lineE = f.readline()
    lineF = f.readline()
    lineG = f.readline()
    lineH = f.readline()
    lineI = f.readline()


column0 = makeColumn(lineA, lineB, lineC, lineD, lineE, lineF, lineG, lineH, lineI, 0)
column1 = makeColumn(lineA, lineB, lineC, lineD, lineE, lineF, lineG, lineH, lineI, 1)
column2 = makeColumn(lineA, lineB, lineC, lineD, lineE, lineF, lineG, lineH, lineI, 2)
column3 = makeColumn(lineA, lineB, lineC, lineD, lineE, lineF, lineG, lineH, lineI, 3)
column4 = makeColumn(lineA, lineB, lineC, lineD, lineE, lineF, lineG, lineH, lineI, 4)
column5 = makeColumn(lineA, lineB, lineC, lineD, lineE, lineF, lineG, lineH, lineI, 5)
column6 = makeColumn(lineA, lineB, lineC, lineD, lineE, lineF, lineG, lineH, lineI, 6)
column7 = makeColumn(lineA, lineB, lineC, lineD, lineE, lineF, lineG, lineH, lineI, 7)
column8 = makeColumn(lineA, lineB, lineC, lineD, lineE, lineF, lineG, lineH, lineI, 8)





#Make sudoku board in a way that can be itorated through
grid = []

grid.append(lineA)
grid.append(lineB)
grid.append(lineC)
grid.append(lineD)
grid.append(lineE)
grid.append(lineF)
grid.append(lineG)
grid.append(lineH)
grid.append(lineI)



#Make sudoku board in a way that can be itorated through
sidewaysGrid = []

sidewaysGrid.append(column0)
sidewaysGrid.append(column1)
sidewaysGrid.append(column2)
sidewaysGrid.append(column3)
sidewaysGrid.append(column4)
sidewaysGrid.append(column5)
sidewaysGrid.append(column6)
sidewaysGrid.append(column7)
sidewaysGrid.append(column8)

#Manually instruct program to calculate possibilities for a board position
lineA_Column0 = checkExistingValues_ROW(lineA)
lineA_Column0.extend(checkExistingValues_SMALL_SQ(lineA, lineB, lineC))
lineA_Column0.extend(checkExistingValues_ROW(column0))





#This section iterates through line A looking for em
coordinateBasedNegative = []
coordinateBasedNegative.append(takeThreeRemoveDuplicate(checkExistingValues_ROW(grid[0]), checkExistingValues_COL(grid, 0) , checkExistingValuesSmallGrid(grid, 0) ))
print(coordinateBasedNegative)
#print(coordinateBasedNegative[0].__len__())

#checkExistingValues_ROW(sidewaysGrid[0])

#printGrid(grid)

#print(grid[2])


#print(checkExistingValuesSmallGrid(grid, 8))

possibleValues = tallyPossibleValuesFullGrid(grid)


z=open('EditThisFile.txt', 'w')
z.write(grid[0])
z.write(grid[1])
z.write(grid[2])
z.write(grid[3])
z.write(grid[4])
z.write(grid[5])
z.write(grid[6])
z.write(grid[7])
z.write(grid[8])
z.close()


placeHolder = []
testString = ''
testString2 = ''
testRow = ''
testCol = ''
f=open("Tally_Values.txt", "r")
sudoku=open('waveComplete.txt', 'w')
if f.mode == 'r':
    p = 0
    k = 0
    e = 0
    while p < 81:
        testString = f.readline()
        testString2 = f.readline()
        print(testString)
        print(testString[15] + " " + testString[18])
        print(testString2)
        print(testString2.count('-'))
        if testString2.count('-') == 8:
            #print('consider this NUMBER!\n')
            #print(testString2[2])
            #print(testString2)
            while k < 45:
                if testString2[k] == '1':
                    print(testString2[k] + ' <<<<<<<<<<<<<< LOOOK!')
                    if grid[int(testString[15])][int(testString[18])] == '-':
                        print("SWAP THIS NUMBER <<<<<<<<<<<<<<<<<<<<<<<<<")
                        u=open('EditThisFile.txt', 'r')
                        placeHolder = []
                        placeHolder.append(u.readlines())
                        u.close()
                        #placeHolder[0][int(testString[15])][int(testString[18])] = testString2[k]
                        makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])
                        z = open('EditThisFile.txt', 'w')
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[0])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[1])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[2])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[3])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[4])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[5])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[6])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[7])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[8])
                        z.close()
                if testString2[k] == '2':
                    print(testString2[k] + ' <<<<<<<<<<<<<< LOOOK!')
                    if grid[int(testString[15])][int(testString[18])] == '-':
                        print("SWAP THIS NUMBER <<<<<<<<<<<<<<<<<<<<<<<<<")
                        u=open('EditThisFile.txt', 'r')
                        placeHolder = []
                        placeHolder.append(u.readlines())
                        u.close()
                        #placeHolder[0][int(testString[15])][int(testString[18])] = testString2[k]
                        makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])
                        z = open('EditThisFile.txt', 'w')
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[0])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[1])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[2])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[3])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[4])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[5])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[6])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[7])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[8])
                        z.close()
                if testString2[k] == '3':
                    print(testString2[k] + ' <<<<<<<<<<<<<< LOOOK!')
                    if grid[int(testString[15])][int(testString[18])] == '-':
                        print("SWAP THIS NUMBER <<<<<<<<<<<<<<<<<<<<<<<<<")
                        u=open('EditThisFile.txt', 'r')
                        placeHolder = []
                        placeHolder.append(u.readlines())
                        u.close()
                        #placeHolder[0][int(testString[15])][int(testString[18])] = testString2[k]
                        makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])
                        z = open('EditThisFile.txt', 'w')
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[0])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[1])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[2])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[3])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[4])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[5])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[6])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[7])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[8])
                        z.close()
                if testString2[k] == '4':
                    print(testString2[k] + ' <<<<<<<<<<<<<< LOOOK!')
                    if grid[int(testString[15])][int(testString[18])] == '-':
                        print("SWAP THIS NUMBER <<<<<<<<<<<<<<<<<<<<<<<<<")
                        u=open('EditThisFile.txt', 'r')
                        placeHolder = []
                        placeHolder.append(u.readlines())
                        u.close()
                        #placeHolder[0][int(testString[15])][int(testString[18])] = testString2[k]
                        makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])
                        z = open('EditThisFile.txt', 'w')
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[0])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[1])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[2])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[3])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[4])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[5])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[6])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[7])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[8])
                        z.close()
                if testString2[k] == '5':
                    print(testString2[k] + ' <<<<<<<<<<<<<< LOOOK!')
                    if grid[int(testString[15])][int(testString[18])] == '-':
                        print("SWAP THIS NUMBER <<<<<<<<<<<<<<<<<<<<<<<<<")
                        u=open('EditThisFile.txt', 'r')
                        placeHolder = []
                        placeHolder.append(u.readlines())
                        u.close()
                        #placeHolder[0][int(testString[15])][int(testString[18])] = testString2[k]
                        makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])
                        z = open('EditThisFile.txt', 'w')
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[0])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[1])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[2])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[3])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[4])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[5])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[6])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[7])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[8])
                        z.close()
                if testString2[k] == '6':
                    print(testString2[k] + ' <<<<<<<<<<<<<< LOOOK!')
                    if grid[int(testString[15])][int(testString[18])] == '-':
                        print("SWAP THIS NUMBER <<<<<<<<<<<<<<<<<<<<<<<<<")
                        u=open('EditThisFile.txt', 'r')
                        placeHolder = []
                        placeHolder.append(u.readlines())
                        u.close()
                        #placeHolder[0][int(testString[15])][int(testString[18])] = testString2[k]
                        makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])
                        z = open('EditThisFile.txt', 'w')
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[0])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[1])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[2])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[3])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[4])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[5])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[6])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[7])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[8])
                        z.close()
                if testString2[k] == '7':
                    print(testString2[k] + ' <<<<<<<<<<<<<< LOOOK!')
                    if grid[int(testString[15])][int(testString[18])] == '-':
                        print("SWAP THIS NUMBER <<<<<<<<<<<<<<<<<<<<<<<<<")
                        u=open('EditThisFile.txt', 'r')
                        placeHolder = []
                        placeHolder.append(u.readlines())
                        u.close()
                        #placeHolder[0][int(testString[15])][int(testString[18])] = testString2[k]
                        makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])
                        z = open('EditThisFile.txt', 'w')
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[0])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[1])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[2])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[3])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[4])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[5])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[6])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[7])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[8])
                        z.close()
                if testString2[k] == '8':
                    print(testString2[k] + ' <<<<<<<<<<<<<< LOOOK!')
                    if grid[int(testString[15])][int(testString[18])] == '-':
                        print("SWAP THIS NUMBER <<<<<<<<<<<<<<<<<<<<<<<<<")
                        u=open('EditThisFile.txt', 'r')
                        placeHolder = []
                        placeHolder.append(u.readlines())
                        u.close()
                        #placeHolder[0][int(testString[15])][int(testString[18])] = testString2[k]
                        makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])
                        z = open('EditThisFile.txt', 'w')
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[0])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[1])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[2])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[3])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[4])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[5])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[6])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[7])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[8])
                        z.close()
                if testString2[k] == '9':
                    print(testString2[k] + ' <<<<<<<<<<<<<< LOOOK!')
                    if grid[int(testString[15])][int(testString[18])] == '-':
                        print("SWAP THIS NUMBER <<<<<<<<<<<<<<<<<<<<<<<<<")
                        u=open('EditThisFile.txt', 'r')
                        placeHolder = []
                        placeHolder.append(u.readlines())
                        u.close()
                        #placeHolder[0][int(testString[15])][int(testString[18])] = testString2[k]
                        makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])
                        z = open('EditThisFile.txt', 'w')
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[0])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[1])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[2])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[3])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[4])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[5])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[6])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[7])
                        z.write(makeNewGrid(placeHolder, int(testString[15]), int(testString[18]), testString2[k])[8])
                        z.close()
                k = k + 1

        p = p + 1
        k = 0

print(grid)
print(grid[0])
print(grid[0][7])
print(placeHolder)
print(placeHolder[0])
print(placeHolder[0][0])
print(placeHolder[0][0][8])
print(placeHolder[0][1][8])
print(placeHolder[0][1][8])
