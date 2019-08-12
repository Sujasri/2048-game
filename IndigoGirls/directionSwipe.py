""""
    This function swipes the tiles in the 2048 game according
    to the direction passed as an input and calculates the
    score of the user and returns the dictionary.


    Created on 16,November

    @author : Sujasri
"""
import math
import random

#Probability function to generate a random value on the resultant board
def probCheck(newDictionary):
    my_list = range(0, len(newDictionary['board']['grid']))
    pos = random.sample(my_list, 1)
    probDictionary = {1: 0.75, 2: 0.25}
    r = random.uniform(0, 1)
    probability = 0
    for j in probDictionary:
        probability = probability + probDictionary[j]
        if probability > r: break
    result = j
    for i in range(0, len(newDictionary['board']['grid'])):
        if newDictionary['board']['grid'][pos[0]] == 0:
            newDictionary['board']['grid'][pos[0]] = result
            break
        else:
            pos = random.sample(my_list, 1)
    return newDictionary

# Converting the matrix into a list
def toMatrix(matrix, messageDictionary, newDictionary):
    for i in range(0, messageDictionary['board']['rowCount']):
        for j in range(0, messageDictionary['board']['columnCount']):
            newDictionary['board']['grid'].append(matrix[i][j])
    newDictionary['board']['rowCount'] = messageDictionary['board']['rowCount']
    newDictionary['board']['columnCount'] = messageDictionary['board']['columnCount']
    newDictionary['gameStatus'] = "underway"
    # To check if the swipe is valid or not
    if newDictionary['board']['grid'] == messageDictionary['board']['grid']:
        newDictionary['check'] = "Invalid"
    else:
        newDictionary['check'] = "Valid"

#To perform upward swipe
def upDirection(messageDictionary):
    newDictionary = {'score': 0,'board': {'columnCount': None, 'rowCount': None, 'grid': []},
                     'gameStatus': None}
    # Check if the previous swipe was valid
    if messageDictionary['check'] == "Valid":
        newDictionary['score'] = messageDictionary['score']
        newDictionary['direction'] = messageDictionary['direction']
        l = messageDictionary['board']['grid']
        matrix = []
        while l != []:
            matrix.append(l[:messageDictionary['board']['columnCount']])
            l = l[messageDictionary['board']['columnCount']:]
        for i in range(0, messageDictionary['board']['columnCount']):
            for j in range(0, messageDictionary['board']['rowCount']):
                if (matrix[j][i] == 0):
                    for k in range(j + 1, messageDictionary['board']['rowCount']):
                        if (matrix[k][i] != 0):
                            matrix[j][i] = matrix[k][i]
                            matrix[k][i] = 0
                            break

        for i in range(0, messageDictionary['board']['columnCount']):
            j = 0
            for k in range(j + 1, messageDictionary['board']['rowCount']):
                if (matrix[j][i] == matrix[k][i]):
                    if (matrix[j][i] == 0):
                        matrix[j][i] = matrix[j][i] + matrix[k][i]
                        j = j + 1
                        break
                    elif (matrix[j][i] != 0):
                        newDictionary['score'] = newDictionary['score'] + (2 ** matrix[j][i] + 2 ** matrix[k][i])
                        matrix[j][i] = int(math.log(2 ** matrix[j][i] + 2 ** matrix[k][i], 2))
                        matrix[k][i] = 0
                        j = j + 1
                        a = j
                        if (matrix[j][i] == 0):
                            for k in range(a + 1, messageDictionary['board']['rowCount']):
                                if matrix[k][i] != 0:
                                    matrix[a][i] = matrix[k][i]
                                    matrix[k][i] = 0
                                    a = a + 1
                else:
                    j = j + 1
        toMatrix(matrix, messageDictionary, newDictionary)
        newDictionary['gameStatus'] = "underway"
        return newDictionary
    else:
        #If the previous swipe has already got invalid then we do not proceed with that grid
        newDictionary['check'] = "Invalid"
        return newDictionary

#To perform downward swipe
def downDirection(messageDictionary):
    newDictionary = {'score': 0,'board': {'columnCount': None, 'rowCount': None, 'grid': []},
                     'gameStatus': None}
    if messageDictionary['check'] == "Valid":
        newDictionary['score'] = messageDictionary['score']
        newDictionary['direction'] = messageDictionary['direction']
        l = messageDictionary['board']['grid']
        matrix = []
        while l != []:
            matrix.append(l[:messageDictionary['board']['columnCount']])
            l = l[messageDictionary['board']['columnCount']:]
        for i in range(0, messageDictionary['board']['columnCount']):
            for j in list(reversed(range(0, messageDictionary['board']['rowCount']))):
                if (matrix[j][i] == 0):
                    for k in list(reversed(range(0, j))):
                        if (matrix[k][i] != 0):
                            matrix[j][i] = matrix[k][i]
                            matrix[k][i] = 0
                            break

        for i in range(0, messageDictionary['board']['columnCount']):
            j = messageDictionary['board']['rowCount'] - 1
            for k in list(reversed(range(0, j))):
                if (matrix[j][i] == matrix[k][i]):
                    if (matrix[j][i] == 0):
                        matrix[j][i] = matrix[j][i] + matrix[k][i]
                        j = j - 1
                        break
                    elif (matrix[j][i] != 0):
                        newDictionary['score'] = newDictionary['score'] + (2 ** matrix[j][i] + 2 ** matrix[k][i])
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
        toMatrix(matrix, messageDictionary, newDictionary)
        newDictionary['gameStatus'] = "underway"
        return newDictionary
    else:
        newDictionary['check'] = "Invalid"
        return newDictionary

#To perform leftward swipe
def leftDirection(messageDictionary):
    newDictionary = {'score': 0,'board': {'columnCount': None, 'rowCount': None, 'grid': []},
                     'gameStatus': None}
    if messageDictionary['check'] == "Valid":
        newDictionary['score'] = messageDictionary['score']
        newDictionary['direction'] = messageDictionary['direction']
        l = messageDictionary['board']['grid']
        matrix = []
        while l != []:
            matrix.append(l[:messageDictionary['board']['columnCount']])
            l = l[messageDictionary['board']['columnCount']:]
        for i in range(0, messageDictionary['board']['rowCount']):
            for j in range(0, messageDictionary['board']['columnCount']):
                if (matrix[i][j] == 0):
                    for k in range(j + 1, messageDictionary['board']['columnCount']):
                        if (matrix[i][k] != 0):
                            matrix[i][j] = matrix[i][k]
                            matrix[i][k] = 0
                            break

        for i in range(0, messageDictionary['board']['rowCount']):
            j = 0
            for k in range(j + 1, messageDictionary['board']['columnCount']):
                if (matrix[i][j] == matrix[i][k]):
                    if (matrix[i][j] == 0):
                        matrix[i][j] = matrix[i][j] + matrix[i][k]
                        j = j + 1
                        break
                    elif (matrix[i][j] != 0):
                        newDictionary['score'] = newDictionary['score'] + (2 ** matrix[i][j] + 2 ** matrix[i][k])
                        matrix[i][j] = int(math.log(2 ** matrix[i][j] + 2 ** matrix[i][k], 2))
                        matrix[i][k] = 0
                        j = j + 1
                        a = j
                        if (matrix[i][j] == 0):
                            for k in range(a + 1, messageDictionary['board']['columnCount']):
                                if matrix[i][k] != 0:
                                    matrix[i][a] = matrix[i][k]
                                    matrix[i][k] = 0
                                    a = a + 1
                else:
                    j = j + 1
        toMatrix(matrix, messageDictionary, newDictionary)
        newDictionary['gameStatus'] = "underway"
        return newDictionary
    else:
        newDictionary['check'] = "Invalid"
        return newDictionary

#To perform rightward move
def rightDirection(messageDictionary):
    newDictionary = {'score': 0,'board': {'columnCount': None, 'rowCount': None, 'grid': []},
                     'gameStatus': None}
    if messageDictionary['check'] == "Valid":
        newDictionary['score'] = messageDictionary['score']
        newDictionary['direction'] = messageDictionary['direction']
        l = messageDictionary['board']['grid']
        matrix = []
        while l != []:
            matrix.append(l[:messageDictionary['board']['columnCount']])
            l = l[messageDictionary['board']['columnCount']:]
        for i in range(0, messageDictionary['board']['rowCount']):
            for j in list(reversed(range(0, messageDictionary['board']['columnCount']))):
                if (matrix[i][j] == 0):
                    for k in list(reversed(range(0, j))):
                        if (matrix[i][k] != 0):
                            matrix[i][j] = matrix[i][k]
                            matrix[i][k] = 0
                            break

        for i in range(0, messageDictionary['board']['rowCount']):
            j = messageDictionary['board']['columnCount'] - 1
            for k in list(reversed(range(0, j))):
                if (matrix[i][j] == matrix[i][k]):
                    if (matrix[i][j] == 0):
                        matrix[i][j] = matrix[i][j] + matrix[i][k]
                        j = j - 1
                        break
                    elif (matrix[i][j] != 0):
                        newDictionary['score'] = newDictionary['score'] + (2 ** matrix[i][j] + 2 ** matrix[i][k])

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
        toMatrix(matrix, messageDictionary, newDictionary)
        newDictionary['gameStatus'] = "underway"
        return newDictionary
    else:
        newDictionary['check'] = "Invalid"
        return newDictionary

