""""
    This function swipes the tiles in the 2048 game according
    to the direction passed as an input and calculates the
    score of the user and places the random tile after each swipe.


    Created on 13,October

    @author : Sujasri
"""
import math
import random
import sys
from IndigoGirls.utils import buildErrorString

#A function to generate a random number based on the probability condition in customer needs
def probCheck():
    probDictionary = {1: 0.75, 2: 0.25}
    r = random.uniform(0, 1)
    probability = 0
    for j in probDictionary:
        probability = probability + probDictionary[j]
        if probability > r: break
    return j

#Converting the matrix into a list
def toMatrix(matrix, messageDictionary):

    for i in range(0, rowCount):
        for j in range(0, columnCount):
            newDictionary['board']['grid'].append(matrix[i][j])
    if newDictionary['board']['grid'] != messageDictionary['board']['grid']:
        my_list = range(0, len(newDictionary['board']['grid']))
        pos = random.sample(my_list, 1)
        result = probCheck()
        for i in range(0, len(newDictionary['board']['grid'])):
            if newDictionary['board']['grid'][pos[0]] == 0:
                newDictionary['board']['grid'][pos[0]] = result
                break
            else:
                pos = random.sample(my_list, 1)
    else:
        return buildErrorString("No tiles can be shifted")

# The function to swipe the tiles in the given directions with validations included
def swipe(messageDictionary):
    global newDictionary
    newDictionary = {'score': 0,
        'board': {'columnCount': None, 'rowCount': None, 'grid': []},
        'gameStatus': None}
    if messageDictionary.has_key('board'):
        if messageDictionary['board'].has_key('rowCount'):
            if type(messageDictionary['board']['rowCount']) == int:
                if messageDictionary['board']['rowCount'] > 1 and messageDictionary['board']['rowCount'] <= 100:
                    newDictionary['board']['rowCount'] = messageDictionary['board']['rowCount']
                    if messageDictionary['board'].has_key('columnCount'):
                        if type(messageDictionary['board']['columnCount']) == int:
                            if messageDictionary['board']['columnCount'] > 1 and messageDictionary['board']['columnCount'] <= 100:
                                newDictionary['board']['columnCount'] = messageDictionary['board']['columnCount']
                                numgrid = messageDictionary['board']['rowCount'] * messageDictionary['board']['columnCount']
                                matrix = []
                                count = 0
                                if messageDictionary['board'].has_key('grid'):
                                    if numgrid == len(messageDictionary['board']['grid']):
                                        l = messageDictionary['board']['grid']
                                        for i in l:
                                            if i < 0 or i > (messageDictionary['board']['rowCount']*messageDictionary['board']['columnCount']):
                                                return buildErrorString("Grid elements are not valid")

                                            elif i > 0:
                                                count = count + 1
                                        if count < 2:
                                            return buildErrorString("Invalid grid")
                                        global columnCount
                                        columnCount = messageDictionary['board']['columnCount']
                                        global rowCount
                                        rowCount = messageDictionary['board']['rowCount']
                                        while l != []:
                                            matrix.append(l[:columnCount])
                                            l = l[columnCount:]
                                        if messageDictionary.has_key('direction'):
                                            if messageDictionary['direction'].lower() == "up":
                                                # Upward movement of the tiles
                                                for i in range(0, columnCount):
                                                    for j in range(0, rowCount):
                                                        if (matrix[j ][i] == 0):
                                                            for k in range(j + 1, rowCount):
                                                                if (matrix[k][i] != 0):
                                                                    matrix[j][i] = matrix[k][i]
                                                                    matrix[k][i] = 0
                                                                    break

                                                for i in range(0, columnCount):
                                                    j = 0
                                                    for k in range(j + 1, rowCount):
                                                        if (matrix[j][i] == matrix[k][i]):
                                                            if (matrix[j][i] == 0):
                                                                matrix[j][i] = matrix[j][i] + matrix[k][i]
                                                                j = j + 1
                                                                break
                                                            elif (matrix[j][i] != 0):
                                                                newDictionary['score'] = newDictionary['score'] + (
                                                                    2 ** matrix[j][i] + 2 ** matrix[k][i])
                                                                matrix[j][i] = int(math.log(2 ** matrix[j][i] + 2 ** matrix[k][i], 2))
                                                                matrix[k][i] = 0
                                                                j = j + 1
                                                                a = j
                                                                if (matrix[j][i] == 0):
                                                                    for k in range(a + 1, rowCount):
                                                                        if matrix[k][i] != 0:
                                                                            matrix[a][i] = matrix[k][i]
                                                                            matrix[k][i] = 0
                                                                            a = a + 1
                                                        else:
                                                            j = j + 1

                                            # Downward movement of the tiles
                                            elif messageDictionary['direction'].lower() == "down":
                                                for i in range(0, columnCount):
                                                    for j in list(reversed(range(0, rowCount))):
                                                        if (matrix[j][i] == 0):
                                                            for k in list(reversed(range(0, j))):
                                                                if (matrix[k][i] != 0):
                                                                    matrix[j][i] = matrix[k][i]
                                                                    matrix[k][i] = 0
                                                                    break

                                                for i in range(0, columnCount):
                                                    j = rowCount - 1
                                                    for k in list(reversed(range(0, j))):
                                                        if ( matrix[j][i] == matrix[k][i]):
                                                            if (matrix[j][i] == 0):
                                                                matrix[j][i] = matrix[j][i] + matrix[k][i]
                                                                j = j - 1
                                                                break
                                                            elif (matrix[j][i] != 0):
                                                                newDictionary['score'] = newDictionary['score'] + (
                                                                    2 ** matrix[j][i] + 2 ** matrix[k][i])
                                                                matrix[j][i] = int(math.log(2 ** matrix[j][i] + 2 ** matrix[k][i], 2))
                                                                matrix[k][i] = 0
                                                                j = j - 1
                                                                a = j
                                                                if (matrix[j][i] == 0):
                                                                    for k in list(reversed(range(0, a))):
                                                                        if matrix[k][i] != 0:
                                                                            matrix[a][i] = matrix[k][i]
                                                                            matrix[k][i] = 0
                                                                            a = a - 1
                                                        else:
                                                            j = j - 1

                                            # Leftward movement of the tiles
                                            elif messageDictionary['direction'].lower() == "left":
                                                for i in range(0, rowCount):
                                                    for j in range(0, columnCount):
                                                        if (matrix[i][j] == 0):
                                                            for k in range(j + 1, columnCount):
                                                                if (matrix[i][k] != 0):
                                                                    matrix[i][j] = matrix[i][k]
                                                                    matrix[i][k] = 0
                                                                    break

                                                for i in range(0, rowCount):
                                                    j = 0
                                                    for k in range(j + 1, columnCount):
                                                        if (matrix[i][j] == matrix[i][k]):
                                                            if (matrix[i][j] == 0):
                                                                matrix[i][j] = matrix[i][j] + matrix[i][k]
                                                                j = j + 1
                                                                break
                                                            elif (matrix[i][j] != 0):
                                                                newDictionary['score'] = newDictionary['score'] + (
                                                                    2 ** matrix[i][j] + 2 ** matrix[i][k])
                                                                matrix[i][j] = int(math.log(2 ** matrix[i][j] + 2 ** matrix[i][k], 2))
                                                                matrix[i][k] = 0
                                                                j = j + 1
                                                                a = j
                                                                if (matrix[i][j] == 0):
                                                                    for k in range(a + 1, columnCount):
                                                                        if matrix[i][k] != 0:
                                                                            matrix[i][a] = matrix[i][k]
                                                                            matrix[i][k] = 0
                                                                            a = a + 1
                                                        else:
                                                            j = j + 1

                                            # Rightward movement of the tiles
                                            elif messageDictionary['direction'].lower() == "right":
                                                for i in range(0, rowCount):
                                                    for j in list(reversed(range(0, columnCount))):
                                                        if (matrix[i][j] == 0):
                                                            for k in list(reversed(range(0, j))):
                                                                if (matrix[i][k] != 0):
                                                                    matrix[i][j] = matrix[i][k]
                                                                    matrix[i][k] = 0
                                                                    break

                                                for i in range(0, rowCount):
                                                    j = columnCount - 1
                                                    for k in list(reversed(range(0, j))):
                                                        if (matrix[i][j] == matrix[i][k]):
                                                            if (matrix[i][j] == 0):
                                                                matrix[i][j] = matrix[i][j] + matrix[i][k]
                                                                j = j - 1
                                                                break
                                                            elif (matrix[i][j] != 0):
                                                                newDictionary['score'] = newDictionary['score'] + (
                                                                    2 ** matrix[i][j] + 2 ** matrix[i][k])
                                                                matrix[i][j] = int(math.log(2 ** matrix[i][j] + 2 ** matrix[i][k], 2))
                                                                matrix[i][k] = 0
                                                                j = j - 1
                                                                a = j
                                                                if (matrix[i][j] == 0):
                                                                    for k in list(reversed(range(0, a))):
                                                                        if matrix[i][k] != 0:
                                                                            matrix[i][a] = matrix[i][k]
                                                                            matrix[i][k] = 0
                                                                            a = a - 1
                                                        else:
                                                            j = j - 1
                                            else:
                                                return buildErrorString("Invalid direction")
                                        else:
                                            return buildErrorString("Missing direction")
                                    else:
                                        return buildErrorString("Invalid Board")
                                else:
                                    return buildErrorString("Grid missing")
                            else:
                                return buildErrorString("ColumnCount out of bounds")
                        else:
                            return buildErrorString("ColumnCount should be a integer")
                    else:
                        return buildErrorString("Missing columnCount")
                else:
                    return buildErrorString("RowCount out of bounds")
            else:
                return buildErrorString("RowCount should be a integer")
        else:
            return buildErrorString("Missing rowCount")
    else:
        return buildErrorString ("Missing board")

    matrixResult = toMatrix(matrix, messageDictionary)
    if matrixResult:
        return matrixResult
    newDictionary['gameStatus'] = "underway"
    return newDictionary



