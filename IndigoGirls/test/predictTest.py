""""
    This is to test the predict function

    Created on 08,December

    @author : Sujasri
"""

from unittest import TestCase
from IndigoGirls.predict import predict
import IndigoGirls.dispatch as IndigoGirls
import json

class predictTest(TestCase):

    #Happy path
    #For moves1

    def test_100ForMove1(self):
        messageDictionary = {'op':'predict', 'direction':'left','moves':1, 'board': {'columnCount': 4, 'rowCount': 4, 'grid': [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}
        predictDictionary = predict(messageDictionary)
        highScore = predictDictionary['prediction']['highScore']
        lowScore = predictDictionary['prediction']['lowScore']
        avgScore = predictDictionary['prediction']['averageScore']
        self.assertEquals(highScore,16)
        self.assertEquals(lowScore, 16)
        self.assertEquals(avgScore, 16)

    def test_110ForMove1(self):
        messageDictionary = {'op':'predict', 'direction':'right','moves':1, 'board': {'columnCount': 4, 'rowCount': 4, 'grid': [0,0,0,1,0,0,0,1,2,1,0,0,1,0,2,2]}}
        predictDictionary = predict(messageDictionary)
        highScore = predictDictionary['prediction']['highScore']
        lowScore = predictDictionary['prediction']['lowScore']
        avgScore = predictDictionary['prediction']['averageScore']
        self.assertEquals(highScore,8)
        self.assertEquals(lowScore, 8)
        self.assertEquals(avgScore, 8)

    def test_130ForMove1(self):
        messageDictionary = {'op':'predict', 'direction':'right','moves':1, 'board': {'columnCount': 4, 'rowCount': 4, 'grid': [1,2,3,4,4,3,2,1,3,4,5,6,1,2,0,0]}}
        predictDictionary = predict(messageDictionary)
        highScore = predictDictionary['prediction']['highScore']
        lowScore = predictDictionary['prediction']['lowScore']
        avgScore = predictDictionary['prediction']['averageScore']
        self.assertEquals(highScore,0)
        self.assertEquals(lowScore,0)
        self.assertEquals(avgScore,0)

    #Happy paths
    #For moves2

    def test_200ForMove2(self):
        messageDictionary = {'op':'predict', 'direction':'right','moves':2, 'board': {'columnCount': 4, 'rowCount': 4, 'grid': [1,2,3,4,4,3,2,1,3,4,5,6,1,2,0,0]}}
        predictDictionary = predict(messageDictionary)
        highScore = predictDictionary['prediction']['highScore']
        lowScore = predictDictionary['prediction']['lowScore']
        avgScore = predictDictionary['prediction']['averageScore']
        self.assertEquals(highScore,4)
        self.assertEquals(lowScore,0)
        self.assertEquals(avgScore,2)

    def test_210ForMove2(self):
        messageDictionary = {'op':'predict', 'direction':'left','moves':2, 'board': {'columnCount': 4, 'rowCount': 4, 'grid': [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}
        predictDictionary = predict(messageDictionary)
        highScore = predictDictionary['prediction']['highScore']
        lowScore = predictDictionary['prediction']['lowScore']
        avgScore = predictDictionary['prediction']['averageScore']
        self.assertEquals(highScore,20)
        self.assertEquals(lowScore,16)
        self.assertEquals(avgScore,19)

    def test_220ForMove2(self):
        messageDictionary = {'op':'predict', 'direction':'up','moves':2, 'board': {'columnCount': 3, 'rowCount': 4, 'grid': [4,0,0,2,1,2,3,3,1,1,2,3]}}
        predictDictionary = predict(messageDictionary)
        highScore = predictDictionary['prediction']['highScore']
        lowScore = predictDictionary['prediction']['lowScore']
        avgScore = predictDictionary['prediction']['averageScore']
        self.assertEquals(highScore,8)
        self.assertEquals(lowScore,0)
        self.assertEquals(avgScore,3)

    #For Validation
    #Sad paths

    def test_300ForValidation(self):
        messageDictionary = {'op': 'predict', 'moves': 1,
                             'board': {'columnCount': 4, 'rowCount': 4,
                                       'grid': [1, 2, 3, 4, 4, 3, 2, 1, 1, 2, 3, 4, 4, 3, 2, 1]}}
        self.assertTrue('error' in json.loads(IndigoGirls.dispatch(messageDictionary))['gameStatus'])

    def test_310ForValidation(self):
        messageDictionary = {'op': 'predict', 'moves': '1', 'board': {'columnCount': 4, 'rowCount': 4,
                                                                        'grid': [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2,
                                                                                 0, 0, 0, 2]}}
        self.assertTrue('error' in json.loads(IndigoGirls.dispatch(messageDictionary))['gameStatus'])

    def test_320ForValidation(self):
        messageDictionary = {'op': 'predict','moves': 1, 'board': {'columnCount': 4, 'rowCount': 4,'grid': [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2,
                                                                                 0, 0, 0, 2]}}

        self.assertTrue('error' in json.loads(IndigoGirls.dispatch(messageDictionary))['gameStatus'])




