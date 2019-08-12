import IndigoGirls.dispatch as dispatch

validJson = '{"op": "initializeGame"}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))


errorJson = '{"op": "unknown"}'
errorResult = dispatch.dispatch(errorJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n\n").format(errorJson, errorResult))


