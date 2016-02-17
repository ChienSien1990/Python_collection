def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    b=True
    cwL = hand.copy()
    if word in wordList and word !='':
       for x in word:
           if x in cwL:
                b=True
           else:
                b=False
                break

    else:
       b = False
    if b == True:
        for x in word:
            if cwL[x]==0:        
                b=False
                break   
            else:
                cwL[x]=cwL.get(x,0)-1
    return b
       
