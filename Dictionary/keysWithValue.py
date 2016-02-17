def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
  
    # Your code here  
    for x in list(aDict.keys()):
        if aDict[x] !=target:
            del aDict[x]
     
    return sorted(aDict.keys())