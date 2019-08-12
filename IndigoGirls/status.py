""""
    This function checks for the status of the game and returns the
    status to the user

    Created on 09,Novermber

    @author : Sujasri
"""
from IndigoGirls.validate import validate
from IndigoGirls.recommend import upDirection
from IndigoGirls.recommend import downDirection
from IndigoGirls.recommend import leftDirection
from IndigoGirls.recommend import rightDirection
from IndigoGirls.utils import buildErrorString

#To find the status of the game
def status(messageDictionary):
    #To check if the grid satisfies the condition for 'win'
    def checkWin(messageDictionary):
        for i in messageDictionary['board']['grid']:
            if pow(2, i) >= messageDictionary['tile']:
                return 1

    #To check the status of the game
    def checkStatus(messageDictionary):
        dictionary ={}
        if checkWin(messageDictionary) == 1:
            dictionary['gameStatus'] = "win"
            return dictionary
        else:
            messageDictionary['score'] =0
            messageDictionary['check'] = "Valid"
            messageDictionary['direction'] = None
            input1 = upDirection(messageDictionary)
            input2 = downDirection(messageDictionary)
            input3 = leftDirection(messageDictionary)
            input4 = rightDirection(messageDictionary)
            # If all the directions on swipe become invalid...then becomes 'lose'
            if input1['check'] == "Invalid" and input2['check'] == "Invalid" and input3['check'] == "Invalid" and input4['check'] == "Invalid":
                dictionary['gameStatus'] = "lose"
                return dictionary
            else:
                dictionary['gameStatus'] = "underway"
                return dictionary

    #The function to validate the input dictionary is called
    errorString = validate(messageDictionary)
    if validate(messageDictionary)==1:
        if messageDictionary.has_key('tile') and type(messageDictionary['tile']) == int and messageDictionary[
            'tile'] >= 2 and messageDictionary['tile'] <= pow(2, (messageDictionary['board']['rowCount'] * messageDictionary['board']['columnCount'])):
            dictionary = checkStatus(messageDictionary)
            return dictionary
        elif not messageDictionary.has_key('tile'):
            messageDictionary['tile'] = pow(2, round(messageDictionary['board']['rowCount'] * messageDictionary['board']['columnCount'] * 0.6875))
            dictionary = checkStatus(messageDictionary)
            return dictionary
        else:
            return buildErrorString("Invalid tile value")
    return errorString


#43



