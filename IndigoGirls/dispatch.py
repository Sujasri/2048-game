import json
from IndigoGirls.initializeGame import initializeGame  # importing the file which contains the initializeGame function
from IndigoGirls.swipe import swipe                    # importing the file which contains the swipe function
from IndigoGirls.recommend import recommend            # importing the file which contains the recommend function
from IndigoGirls.status import status                  # importing the file which contains the status function
from IndigoGirls.predict import predict                # importing the file which contains the predict function

def buildErrorString(diagnostic=None):
    """
        returns a dictionary containing the specified key and accompanying diagnostic information
        :param
            diagnostic:     A string that describes the error
        :return:    A dictionary that contains the specified error key having a value that
                    consists of the specfied error string followed by a free-form diagnostic message
    """
    ERROR_PROPERTY = u'gameStatus'
    ERROR_PREFIX = u'error:  '
    return {ERROR_PROPERTY: ERROR_PREFIX + diagnostic}

def dispatch(messageJson=None):
    """
        dispatch is the microservice dispatcher for IndigoGirls, a 2048-like game.  It routes
        requests for game state transformations to the appropriate functions
        :param
            messageJson: JSON string that describes the state of the game needed for the
                        requested transformation
            :return:    A JSON string that describes the state of the game after the requested transformation
                        has taken place.
    """

    #Validate JSONness of input be converting the string to an equivalent dictionary
    try:

        messageDictionary = json.loads(messageJson)
    except:
        resultDictionary = json.dumps(buildErrorString('input JSON string is invalid'))
        return resultDictionary

    #Validate presence of dispatching code
    if(u"op" not in messageDictionary):
        resultDictionary = json.dumps(buildErrorString('op is missing'))
        return resultDictionary

    #Perform the game transformation as directed by the value of the "op" key
    #  input to each function:  a dictionary containing the name-value pairs of the input JSON string
    #  output of each function:  a dictionary containing name-value pairs to be encoded as a JSON string
    if(messageDictionary[u"op"] == u"initializeGame"):
        resultDictionary =initializeGame(messageDictionary)
    elif (messageDictionary[u"op"] == u"swipe"):
        resultDictionary = swipe(messageDictionary)
    elif (messageDictionary[u"op"] == u"recommend"):
        resultDictionary = recommend(messageDictionary)
    elif (messageDictionary[u"op"] == u"status"):
        resultDictionary = status(messageDictionary)
    elif (messageDictionary[u"op"] == u"predict"):
        resultDictionary = predict(messageDictionary)
    else:
        resultDictionary = buildErrorString('op is invalid')

    #Convert the dictionary back to a string in JSON format
    resultJson = json.dumps(resultDictionary)
    return resultJson