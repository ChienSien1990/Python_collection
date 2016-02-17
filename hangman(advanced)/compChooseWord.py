def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    maxsc=0
    
    # Create a new variable to store the best word seen so far (initially None)  
    maxwrd=None
    # For each word in the wordList
    for x in wordList:
        if isValidWord(x,hand,wordList):
            if maxsc<getWordScore(x,n):
                maxsc=getWordScore(x,n)
                maxwrd=x
    return maxwrd
