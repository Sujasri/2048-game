from unittest import TestCase
from IndigoGirls.recommend import recommend
import IndigoGirls.dispatch as IndigoGirls
import json

class recommendTest(TestCase):

    # For moves when not specified or specified 0
    # Happy path

    for i in range(0, 10):  # Running for a number of times as it has the random function to generate the results
        def test_100For0Moves(self):
            result = {}
            messageDictionary = {'op': 'recommend', 'moves': 0,
                                 'board': {'columnCount': 4, 'rowCount': 4,
                                           'grid': [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2]}}
            score = [8, 0]
            result = recommend(messageDictionary)
            self.assertIn(result['score'], score)

        def test_110For0Moves(self):
            result = {}
            messageDictionary = {'op': 'recommend',
                                 'board': {'columnCount': 4, 'rowCount': 4,
                                           'grid': [0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 0, 0, 1, 0, 2, 2]}}

            score = [16, 4]
            result = recommend(messageDictionary)
            self.assertIn(result['score'], score)

        def test_120For0Moves(self):
            result = {}
            messageDictionary = {'op': 'recommend', 'moves': 0,
                                 'board': {'columnCount': 4, 'rowCount': 4,
                                           'grid': [0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 0, 0, 1, 0, 2, 2]}}
            score = [16, 4]
            result = recommend(messageDictionary)
            self.assertIn(result['score'], score)

    # For 1 move
    # Happy path

    for i in range(0, 20):
        def test_300For1Move(self):
            result = {}
            messageDictionary = {'op': 'recommend', "moves": 1,
                                 'board': {'columnCount': 4, 'rowCount': 4,
                                           'grid': [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2]}}
            score = 8
            result = recommend(messageDictionary)
            self.assertEquals(result['score'], score)

    for i in range(0, 20):
        def test_310For1Move(self):
            result = {}
            messageDictionary = {'op': 'recommend', "moves": 1,
                                 'board': {'columnCount': 4, 'rowCount': 4,
                                           'grid': [0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 0, 0, 1, 0, 2, 2]}}
            score = 16
            result = recommend(messageDictionary)
            self.assertEquals(result['score'], score)

    for i in range(0, 20):
        def test_320For1Move(self):
            result = {}
            messageDictionary = {'op': 'recommend', "moves": 1,
                                 'board': {'columnCount': 4, 'rowCount': 4,
                                           'grid': [0, 0, 0, 2, 0, 0, 0, 2, 4, 4, 0, 0, 2, 0, 4, 4]}}
            score = 64
            result = recommend(messageDictionary)
            self.assertEquals(result['score'], score)

    #For 2 moves
    #Happy path

    for i in range(0,20):
        def test_400For2Moves(self):
            result={}
            messageDictionary = {'op': 'recommend', "moves": 2,
                                 'board': {'columnCount': 4, 'rowCount': 4,
                                           'grid': [0,0,0,2,0,0,0,2,4,4,0,0,2,0,4,4]}}
            score = 64
            result = recommend(messageDictionary)
            self.assertEquals(result['score'],score)

    for i in range(0, 20):
        def test_410For2Moves(self):
            result = {}
            messageDictionary = {'op': 'recommend', "moves": 2,
                                 'board': {'columnCount': 4, 'rowCount': 4,
                                           'grid': [1,1,2,1,2,1,1,1,2,2,1,1,0,1,2,2]}}
            score = 28
            result = recommend(messageDictionary)
            self.assertEquals(result['score'], score)

    for i in range(0, 20):
        def test_420For2Moves(self):
            result = {}
            messageDictionary = {'op': 'recommend', "moves": 2,
                                 'board': {'columnCount': 4, 'rowCount': 4,
                                           'grid': [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}
            score = 16
            result = recommend(messageDictionary)
            self.assertEquals(result['score'], score)

        def test_430For2Moves(self):
            result = {}
            messageDictionary = {'op': 'recommend', "moves": 2,
                                 'board': {'columnCount': 4, 'rowCount': 4,
                                           'grid': [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}
            score = 16
            result = recommend(messageDictionary)
            self.assertEquals(result['score'], score)

    #For 3 moves

    def test_440For3Moves(self):
        result = {}
        messageDictionary = {'op': 'recommend', "moves": 3,
                             'board': {'columnCount': 4, 'rowCount': 4,
                                       'grid': [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}
        result = recommend(messageDictionary)
        score = 16
        self.assertEquals(result['score'], score)

    # #For Validation
    # #Sad paths

    def test_500ForValidation(self):

        messageDictionary ={'op': 'recommend', 'moves': 1,
         'board': {'columnCount': 4, 'rowCount': 4, 'grid': [1, 2, 3, 4, 4, 3, 2, 1, 1, 2, 3, 4, 4, 3, 2, 1]}}
        self.assertTrue('error' in json.loads(IndigoGirls.dispatch(messageDictionary))['gameStatus'])

    def test_600ForValidation(self):
        messageDictionary = {'op': 'recommend','moves': '1', 'board': {'columnCount': 4, 'rowCount': 4,
                                                          'grid': [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2]}}
        self.assertTrue('error' in json.loads(IndigoGirls.dispatch(messageDictionary))['gameStatus'])






