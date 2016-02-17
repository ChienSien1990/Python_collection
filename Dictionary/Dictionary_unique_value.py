def chkdic(cDict,val):
    a=0
    for x in cDict.keys():
        if val == cDict[x]:
            a=x
            break
    return a
            
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    lists=[]
    cDict={}
    for key in aDict.keys():
                if not aDict[key] in cDict.values():
                    cDict[key]=aDict[key]
                    lists.append(key)
                else:
                    if( chkdic(cDict,aDict[key]) in lists):
                        lists.remove(chkdic(cDict,aDict[key]))
                    cDict[key]=aDict[key]
                    del cDict[chkdic(cDict,aDict[key])]
    lists.sort()
    return lists