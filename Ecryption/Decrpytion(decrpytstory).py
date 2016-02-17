def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    sth=0
    char=''
    str1=""
    sstring=[]
    for i in text:
        if (not i in string.ascii_lowercase and not i in string.ascii_uppercase):
            char=i
            break;
    if(char!=''):
        sstring=text.split(char)
        str1="".join(sstring[0])
    else:
        sstring.append(text)
        str1="".join(sstring)
    for x in range(0,26):
        if(isWord(wordList,applyShift(str1,x))):
            sth=x
            break
    return sth