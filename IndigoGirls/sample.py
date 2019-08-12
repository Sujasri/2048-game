#from IndigoGirls.swipe import swipe
from IndigoGirls.predict import predict
#from IndigoGirls.status import status


messageDictionary = {'op':'predict', 'direction':'Right','moves':2, 'board': {'columnCount': 4, 'rowCount': 4, 'grid': [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}
result = predict(messageDictionary)
print result


# messageDictionary = {'op':'status', 'tile': 32, 'board': {'columnCount': 4, 'rowCount': 4, 'grid': [1,2,3,4,4,3,2,1,1,2,3,4,4,3,2,1]}}
# result = status(messageDictionary)
# print result




