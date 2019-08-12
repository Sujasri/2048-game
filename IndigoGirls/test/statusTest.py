from unittest import TestCase
from IndigoGirls.status import status
import IndigoGirls.dispatch as IndigoGirls
import json

class statusTest(TestCase):

    #Happy path
    #Win
    def test_200ForWin(self):
        messageDictionary = {'op': 'status', 'tile': 16,
                             'board': {'columnCount': 4, 'rowCount': 4,
                                       'grid': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 1, 0]}}
        result = {}
        result['gameStatus'] = "Win"
        self.assertEquals(status(messageDictionary),result)

    def test_210ForWin(self):
        messageDictionary = {'op': 'status', 'tile': 32,
                             'board': {'columnCount': 4, 'rowCount': 4,
                                       'grid': [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 4, 0, 0, 0, 1, 0]}}
        result = {}
        result['gameStatus'] = "Win"
        self.assertEquals(status(messageDictionary),result)

    #Happy path
    #Lose,Underway
    def test_300ForLose(self):
        messageDictionary = {'op': 'status', 'tile': 32,
                             'board': {'columnCount': 4, 'rowCount': 4,
                                       'grid': [1,2,3,4,4,3,2,1,1,2,3,4,4,3,2,1]}}
        result ={}
        result['gameStatus'] = "Lose"
        self.assertEquals(status(messageDictionary),result)

    def test_310ForUnderway(self):
        messageDictionary = {'op': 'status', 'tile': 2048,
                             'board': {'columnCount': 4, 'rowCount': 4,
                                       'grid': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]}}
        result = {}
        result['gameStatus'] = "Underway"
        self.assertEquals(status(messageDictionary),result)

    def test_320ForUnderway(self):
        messageDictionary = {'op': 'status', 'tile': 20,
                             'board': {'columnCount': 4, 'rowCount': 4,
                                       'grid': [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]}}
        result = {}
        result['gameStatus'] = "Underway"
        self.assertEquals(status(messageDictionary),result)

    #Sad Path

    def test_130ForValidation(self):
        messageDictionary = {'op': 'status', 'tile': 'l',
                             'board': {'columnCount': 4, 'rowCount': 4,
                                       'grid': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]}}
        self.assertTrue('error' in json.loads(IndigoGirls.dispatch(messageDictionary))['gameStatus'])

    def test_140ForValidation(self):
        messageDictionary = {'op': 'status', 'tile': 1,
                             'board': {'columnCount': 4, 'rowCount': 4,
                                       'grid': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]}}
        self.assertTrue('error' in json.loads(IndigoGirls.dispatch(messageDictionary))['gameStatus'])

    def test_150ForValidation(self):
        messageDictionary = {'op': 'status', 'tile': 65537,
                             'board': {'columnCount': 4, 'rowCount': 4,
                                       'grid': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]}}
        self.assertTrue('error' in json.loads(IndigoGirls.dispatch(messageDictionary))['gameStatus'])









