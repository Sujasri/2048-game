validJson ='{"op":"initializeGame", "rowCount": 2, "columnCount": 2}'      #Pass
validJson ='{"op":"initializeGame", "rowCount": 2}'                        #Pass
validJson = '{"op":"initializeGame", "rowCount": 2 , "columnCount": 5}'    #Pass
validJson ='{"op":"initializeGame", "rowCount":"two"}'                     #Fail
validJson =  '{"op":"initializeGame", "columnCount":"9"}'                  #Fail
validJson = '{"op":"initializeGame", "columnCount":1}'                     #Fail
validJson = '{"op": "initializeGame":"rowCount":2,"columnCount":"2"}'      #Fail