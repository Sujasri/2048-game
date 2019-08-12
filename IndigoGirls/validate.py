""""
    This function validates the input dictionary
    and returns the error strings where necassary

    Created on 09,November

    @author : Sujasri
"""
from IndigoGirls.utils import buildErrorString

#Function to validate the input dictionary
def validate(messageDictionary):
    if messageDictionary.has_key('board'):
        if messageDictionary['board'].has_key('rowCount'):
            if type(messageDictionary['board']['rowCount']) == int:
                if messageDictionary['board']['rowCount'] > 1 and messageDictionary['board']['rowCount'] <= 100:
                    if messageDictionary['board'].has_key('columnCount'):
                        if type(messageDictionary['board']['columnCount']) == int:
                            if messageDictionary['board']['columnCount'] > 1 and messageDictionary['board'][
                                'columnCount'] <= 100:
                                numgrid = messageDictionary['board']['rowCount'] * messageDictionary['board'][
                                    'columnCount']
                                count = 0
                                if messageDictionary['board'].has_key('grid'):
                                    if numgrid == len(messageDictionary['board']['grid']):
                                        l = messageDictionary['board']['grid']
                                        for i in l:
                                            if i < 0 or i > (messageDictionary['board']['rowCount'] * messageDictionary['board']['columnCount']):
                                                return buildErrorString("Grid elements are not valid")
                                            elif i > 0:
                                                count = count + 1
                                        if count < 2:
                                            return buildErrorString("Invalid grid")
                                        return 1
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
        return buildErrorString("Missing board")
