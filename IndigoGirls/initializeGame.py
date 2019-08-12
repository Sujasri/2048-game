""""
    This function initializes the 2048 game by placing
    2 numbers randomly on the grid that is created from the inputs
    given by the user, so as to initialise the game..

    Created on 18,September

    @author : Sujasri
"""

def initializeGame(messageDictionary):
    import random
    import sys
    from IndigoGirls.dispatch import buildErrorString

    #Creating  a dictionary to output the initialised game
    newDictionary={'score': None,
     'board': {'columnCount':None , 'rowCount': None, 'grid': []},
     'gameStatus':None }

    #Score is set to 0
    newDictionary["score"]= messageDictionary.setdefault('score', 0)

    #Validating the input rowCount and displaying  errors if any
    if messageDictionary.has_key('rowCount'):
        if type(messageDictionary['rowCount'])== int:
            if messageDictionary['rowCount'] > 1 and messageDictionary['rowCount'] <= 100:
                newDictionary['board']['rowCount'] = messageDictionary['rowCount']

            else:

                return buildErrorString("rowCount is out of bounds")
                sys.exit(1)
        else:

            return buildErrorString("rowCount is not an integer")
            sys.exit(1)
    else:
        newDictionary['board']['rowCount'] = 4

    #Validating the input columnCount and displaying errors if any
    if messageDictionary.has_key('columnCount'):
        if type(messageDictionary['columnCount'])== int:
            if messageDictionary['columnCount'] > 1 and messageDictionary['columnCount'] <= 100:
                newDictionary['board']['columnCount'] = messageDictionary['columnCount']

            else:

                return buildErrorString("columnCount is out of bounds")
                sys.exit(1)
        else:

            return buildErrorString("columnCount is not an integer")
            sys.exit(1)
    else:
        newDictionary['board']['columnCount'] = 4

    # Function to assign '1' or '2' depending on the probability in the 'customer needs'
    def probCheck():
        probDictionary = {1 : 0.75, 2:0.25}
        r = random.uniform(0,1)
        probability = 0
        for j in probDictionary:
            probability = probability + probDictionary[j]
            if probability > r: break
        return j

    numgrid = newDictionary['board']['rowCount'] * newDictionary['board']['columnCount']
    my_list=range(1,numgrid+1)
    l = random.sample(my_list, 2)                #<----Generates random numbers to position the non-zero intergers

    #Making up the grid
    for i in my_list:
        if i in l:
            result = probCheck()
            if result == 1:
                newDictionary['board']['grid'].append(1)
            else:
                newDictionary['board']['grid'].append(2)
        else:
            newDictionary['board']['grid'].append(0)

    #Game status is set to 'underway'
    newDictionary['gameStatus'] = messageDictionary.setdefault('gameStatus', 'underway')
    #Returns the dictionary which sets the grid with 2 numbers on it
    return newDictionary



