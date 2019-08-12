from unittest import TestCase
from IndigoGirls.swipe import swipe
import IndigoGirls.dispatch as IndigoGirls
import json

class recommendTest(TestCase):


    # Checking the whole code with validation
    # Happy paths
    # Up , down , left and right directions

    def test_800swipeForUpDirection(self):
        count =0
        messageDictionary = {'op': 'swipe', 'direction': 'up',
                          'board': {'columnCount': 4, 'rowCount': 4,
                                    'grid': [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2]}}
        testgrid = [0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        result = swipe(messageDictionary)
        print result
        for i in range(0,len(testgrid)):
            if testgrid[i] != result['board']['grid'][i]:
                count = count+1
        self.assertEquals(count,1)
        self.assertEquals(result['score'],8)

    def test_801swipeForDownDirection(self):
        count =0
        messageDictionary = {'op': 'swipe', 'direction': 'down',
                          'board': {'columnCount': 4, 'rowCount': 4,
                                    'grid': [1,1, 0, 1, 1, 2, 0, 0, 0, 2, 1, 2, 1, 1, 0, 1]}}
        testgrid = [[0, 0, 0, 0, 0, 1, 0, 1, 1, 3, 0, 2, 2, 1, 1, 1]]
        result = swipe(messageDictionary)
        print result
        for i in range(0,len(testgrid)):
            if testgrid[i] != result['board']['grid'][i]:
                count = count+1
        self.assertEquals(count,1)
        self.assertEquals(result['score'], 12)

    def test_802swipeForLeftDirection(self):
        count =0
        messageDictionary = {'op': 'swipe', 'direction': 'left',
                          'board': {'columnCount': 5, 'rowCount': 4,
                                    'grid': [1,0,1,0,1,0,1,2,0,0,1,0,1,1,1,1,0,1,0,0]}}
        testgrid = [[[2, 1, 0, 0, 0, 1, 2, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0]]]
        result = swipe(messageDictionary)
        print result
        for i in range(0,len(testgrid)):
            if testgrid[i] != result['board']['grid'][i]:
                count = count+1
        self.assertEquals(count,1)
        self.assertEquals(result['score'],16)

    def test_803swipeForRightDirection(self):
        count =0
        messageDictionary = {'op': 'swipe', 'direction': 'right',
                          'board': {'columnCount': 4, 'rowCount': 5,
                                    'grid': [0, 1, 0, 1,2, 0, 0, 2, 2, 2, 0,2, 2, 2, 2, 2, 0, 3, 0, 0]}}
        testgrid = [0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 2, 3, 0, 0, 3, 3, 0, 0, 0, 3]
        result = swipe(messageDictionary)
        print result
        for i in range(0,len(testgrid)):
            if testgrid[i] != result['board']['grid'][i]:
                count = count+1
        self.assertEquals(count,1)
        self.assertEquals(result['score'],36)

    # Sad paths
    # missing direction, invalid direction , invalid grid , no tiles can be shifted
    # rowCount , columnCount , board - validations

    def test_900Validation(self):
        messageDictionary = {'op': 'swipe',"direction" : "right",
                          'board': {'columnCount': 4, 'rowCount': -4,
                                    'grid': [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2]}}
        self.assertTrue('error' in json.loads(IndigoGirls.dispatch(messageDictionary))['gameStatus'])

    def test_901Validation(self):
        messageDictionary = {'op': 'swipe',
                          'board': {'columnCount': 4, 'rowCount': 4,
                                    'grid': [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2]}}
        self.assertTrue('error' in json.loads(IndigoGirls.dispatch(messageDictionary))['gameStatus'])

    def test_902Validation(self):
        messageDictionary = {'op': 'swipe', 'direction' : 'right',
                          'board': {'columnCount': 4, 'rowCount': 4,
                                    'grid': [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0]}}
        self.assertTrue('error' in json.loads(IndigoGirls.dispatch(messageDictionary))['gameStatus'])

    def test_903Validation(self):
        messageDictionary = {'op': 'swipe', 'direction' : 'r',
                          'board': {'columnCount': 4, 'rowCount': 4,
                                    'grid': [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0,0,0,1]}}
        self.assertTrue(swipe(messageDictionary),"{u'gameStatus': u'error:  Invalid direction'}")

    def test_904Validation(self):
        messageDictionary = {'op': 'swipe', 'direction' : 'right',
                          'board': {'columnCount': 4, 'rowCount': 4,
                                    'grid': [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0,0,0,1]}}
        self.assertTrue('error' in json.loads(IndigoGirls.dispatch(messageDictionary))['gameStatus'])

    def test_905Validation(self):
        messageDictionary = {'op': 'swipe', 'direction' : 'right',
                          'board': {'columnCount': '4', 'rowCount': 4,
                                    'grid': [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0,0,0,1]}}
        self.assertTrue('error' in json.loads(IndigoGirls.dispatch(messageDictionary))['gameStatus'])
























