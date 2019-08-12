""""
    This function predicts the high,low and average scores
    swiping the tiles in the 2048 game according to the
    given direction and the moves parameter specified


    Created on 08,December

    @author : Sujasri
"""

from IndigoGirls.validate import validate
from IndigoGirls.utils import buildErrorString
from IndigoGirls.predictSwipe import upDirection
from IndigoGirls.predictSwipe import downDirection
from IndigoGirls.predictSwipe import leftDirection
from IndigoGirls.predictSwipe import rightDirection

#To predict the low,average and high scores
def predict(messageDictionary):
    #For validation of the input entries
    errorString = validate(messageDictionary)
    if validate(messageDictionary) == 1:
        score = []
        weights = 0
        highScore = 0
        lowScore = 0
        values = [1, 2]
        weightcounts = 0
        messageDictionary['check'] = "Valid"

        #To swipe in the given direction and calculates its score
        def forMoves1(messageDictionary):
            if messageDictionary['direction'].lower() == "up":
                messageDictionary = dict.copy(upDirection(messageDictionary))
            elif messageDictionary['direction'].lower() == "down":
                messageDictionary = dict.copy(downDirection(messageDictionary))
            elif messageDictionary['direction'].lower() == "left":
                messageDictionary = dict.copy(leftDirection(messageDictionary))
            elif messageDictionary['direction'].lower() == "right":
                messageDictionary = dict.copy(rightDirection(messageDictionary))
            else:
                return 0
            if messageDictionary['check'] == "Valid":
                return messageDictionary
            else:
                return 0

        if messageDictionary.has_key('direction') and type(messageDictionary['direction']) == str:
            if messageDictionary.has_key('moves') and messageDictionary['moves'] == 2 and type(messageDictionary['moves']) == int:
                messageDictionary = forMoves1(messageDictionary)
                if messageDictionary == 0:
                    return buildErrorString("Invalid input")

                else:
                    points = messageDictionary['score']
                    c = 0
                    #To check for the empty cells
                    for i in messageDictionary['board']['grid']:
                        if i == 0:
                            frequency = 3
                            for j in values:
                                messageDictionary['board']['grid'][c] = j
                                upDictionary = dict.copy(upDirection(messageDictionary))
                                if upDictionary['check'] == "Valid":
                                    score.append(upDictionary['score'])
                                    weightcounts = weightcounts + upDictionary['score'] * frequency
                                    weights = weights + frequency

                                downDictionary = dict.copy(downDirection(messageDictionary))
                                if downDictionary['check'] == "Valid":
                                    score.append(downDictionary['score'])
                                    weightcounts = weightcounts + downDictionary['score'] * frequency
                                    weights = weights + frequency

                                leftDictionary = dict.copy(leftDirection(messageDictionary))
                                if leftDictionary['check'] == "Valid":
                                    score.append(leftDictionary['score'])
                                    weightcounts = weightcounts + leftDictionary['score'] * frequency
                                    weights = weights + frequency

                                rightDictionary = dict.copy(rightDirection(messageDictionary))
                                if rightDictionary['check'] == "Valid":
                                    score.append(rightDictionary['score'])
                                    weightcounts = weightcounts + rightDictionary['score'] * frequency
                                    weights = weights + frequency

                                if score!=[] and highScore < max(score) :
                                    highScore = max(score)
                                if score!=[] and lowScore > min(score):
                                    lowScore = min(score)
                                score = []
                                messageDictionary['board']['grid'][c] = 0
                                frequency = frequency - 2
                        c = c + 1

                    if weights == 0:
                        return buildErrorString("Cannot be swiped")
                    averageScore = int(round(weightcounts / float(weights)))
                    highScore = points+ highScore
                    lowScore = points + lowScore
                    averageScore = points + averageScore
                    predictDictionary = {'prediction': {'highScore': highScore, 'lowScore': lowScore, 'averageScore': averageScore},
                                                        'gameStatus': "underway"}
                    return predictDictionary

            elif not messageDictionary.has_key('moves') or messageDictionary['moves']==1:
                messageDictionary['moves'] = 1
                messageDictionary = forMoves1(messageDictionary)
                if messageDictionary == 0:
                    return buildErrorString("Invalid input")
                points = messageDictionary['score']
                predictDictionary = {'prediction': {'highScore': points, 'lowScore': points, 'averageScore': points},'gameStatus': "underway"}
                return predictDictionary

            else:
                return buildErrorString("Invalid moves")
        else:
            return buildErrorString("Invalid direction")
    else:
        return errorString


