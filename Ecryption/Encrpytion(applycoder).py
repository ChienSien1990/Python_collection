def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    myDict={}
    
    for i in string.ascii_lowercase:
        if((ord(i)+shift)>122):
            myDict[i] = chr(ord(i)+shift-26)
        else:
            myDict[i] = chr(ord(i)+shift)
    for i in string.ascii_uppercase:
        if((ord(i)+shift)>90):
            myDict[i] = chr(ord(i)+shift-26)
        else:
            myDict[i] = chr(ord(i)+shift)
    return myDict
