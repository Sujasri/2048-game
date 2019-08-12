""""
    This function recommends the next possible direction by
    swiping the tiles in the 2048 game according to the
    highest score by the moves parameter specified


    Created on 08,November

    @author : Sujasri
"""
import random
from IndigoGirls.utils import buildErrorString
from IndigoGirls.validate import validate
from IndigoGirls.directionSwipe import upDirection
from IndigoGirls.directionSwipe import downDirection
from IndigoGirls.directionSwipe import leftDirection
from IndigoGirls.directionSwipe import rightDirection
from IndigoGirls.directionSwipe import probCheck

#To recommend the next move
def recommend(messageDictionary):
    #Function to validate the input dictionay is called
    errorString = validate(messageDictionary)
    if validate(messageDictionary)== 1:
        messageDictionary['score'] =0
        messageDictionary['check'] ="Valid"
        if messageDictionary.has_key('moves') and messageDictionary['moves'] >= 1 and type(messageDictionary['moves']) == int:
            moves = messageDictionary['moves']
            finalDictionary={}
            temp = 0
            resultDictionary={'check':None}
            global iteration
            iteration = 1
            global input
            input = []

            #To find the highest of the scores
            def findHighest(input1, input2, input3, input4, temp, resultDictionary):
                global finalDictionary
                score = {}
                if input1['check'] == "Valid":
                    score['up'] = input1['score']
                if input2['check'] == "Valid":
                    score['down'] = input2['score']
                if input3['check'] == "Valid":
                    score['left'] = input3['score']
                if input4['check'] == "Valid":
                    score['right'] = input4['score']
                if score != {}:
                    highest = max(score.values())
                    direction = random.choice([k for k, v in score.items() if v == highest])
                    #Checking for each direction if the score is the higest and has got a valid move
                    if direction == 'up' and temp <= input1['score'] and input1['check'] == "Valid":
                        temp = input1['score']
                        finalDictionary = dict.copy(input1)
                        finalDictionary['check'] = 'Valid'
                    elif direction == 'down' and temp <= input2['score'] and input2['check'] == "Valid":
                        temp = input2['score']
                        finalDictionary = dict.copy(input2)
                        finalDictionary['check'] = 'Valid'
                    elif direction == 'left' and temp <= input3['score'] and input3['check'] == "Valid":
                        temp = input3['score']
                        finalDictionary = dict.copy(input3)
                        finalDictionary['check'] = 'Valid'
                    elif direction == 'right' and temp <= input4['score'] and input4[ 'check'] == "Valid":
                        temp = input4['score']
                        finalDictionary = dict.copy(input4)
                        finalDictionary['check'] = 'Valid'
                else:
                    finalDictionary = dict.copy(resultDictionary)
                return finalDictionary, temp

            #Recursive function to swipe the board in all 4 directions depending on the number of moves
            def function(messageDictionary, moves, count, resultDictionary, temp):
                if count < moves:
                    count = count + 1
                    global iteration
                    if iteration == 1:
                        messageDictionary['direction'] = "up"
                    input1 = upDirection(messageDictionary)
                    if iteration == 1:
                        messageDictionary['direction'] = "down"
                    input2 = downDirection(messageDictionary)
                    if iteration == 1:
                        messageDictionary['direction'] = "left"
                    input3 = leftDirection(messageDictionary)
                    if iteration == 1:
                        messageDictionary['direction'] = "right"
                    input4 = rightDirection(messageDictionary)
                    if iteration == 1:
                        global input
                        #'input' dictionary keeps track of the initial 4 dictionaries on swipe,to return the appropriate one at the end
                        input = [input1, input2, input3, input4]
                    iteration = 0
                    if count == moves:
                        resultDictionary, temp = findHighest(input1, input2, input3,input4, temp, resultDictionary)
                    temp, resultDictionary = function(input1, moves, count,resultDictionary, temp)
                    temp, resultDictionary = function(input2, moves, count,resultDictionary, temp)
                    temp, resultDictionary = function(input3, moves, count,resultDictionary, temp)
                    temp, resultDictionary = function(input4, moves, count,resultDictionary, temp)
                return temp, resultDictionary

            count = 0
            temp, resultDictionary = function(messageDictionary, moves, count,resultDictionary, temp)
            #Returning the dictionary with the highest score
            if resultDictionary['check'] == "Valid":
                if resultDictionary['direction'] == "up":
                    resultDictionary = dict.copy(input[0])
                elif resultDictionary['direction'] == "down":
                    resultDictionary = dict.copy(input[1])
                elif resultDictionary['direction'] == "left":
                    resultDictionary = dict.copy(input[2])
                elif resultDictionary['direction'] == "right":
                    resultDictionary = dict.copy(input[3])
                resultDictionary.pop('direction')
                resultDictionary.pop('check')
                resultDictionary = probCheck(resultDictionary)
                return resultDictionary
            else:
                return buildErrorString("No tiles can be shifted")

        #Randomly generating  a direction move if the move is valid for '0' move
        elif not messageDictionary.has_key('moves') or messageDictionary['moves'] == 0:
            directions =[]
            messageDictionary['direction'] = 0
            input1 = upDirection(messageDictionary)
            if input1['check'] == "Valid":
                directions.append("up")
            input2= downDirection(messageDictionary)
            if input2['check'] == "Valid":
                directions.append("down")
            input3 = leftDirection(messageDictionary)
            if input3['check'] == "Valid":
                directions.append("left")
            input4 = rightDirection(messageDictionary)
            if input4['check'] == "Valid":
                directions.append("right")
            if directions != 0:
                randomDirection = random.choice(directions)
                if randomDirection == "up":
                    input1.pop('check')
                    input1.pop('direction')
                    input1 = probCheck(input1)
                    return input1
                if randomDirection == "down":
                    input2.pop('check')
                    input2.pop('direction')
                    input2 = probCheck(input2)
                    return input2
                if randomDirection == "left":
                    input3.pop('check')
                    input3.pop('direction')
                    input3 = probCheck(input3)
                    return input3
                if randomDirection == "right":
                    input4.pop('check')
                    input4.pop('direction')
                    input4 = probCheck(input4)
                    return input4
            else:
                return buildErrorString("No moves")
        else:
            return buildErrorString("Invalid move")
    else :
        return errorString

