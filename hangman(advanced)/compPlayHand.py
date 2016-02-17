def compChooseWord(hand, wordList, n):
    maxsc=0
    maxwrd=None
    for x in wordList:
        if isValidWord(x,hand,wordList):
            if maxsc<getWordScore(x,n):
                maxsc=getWordScore(x,n)
                maxwrd=x
    return maxwrd
    
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    s=''
    b=True
    acc=0
 
    while(b):
        if calculateHandlen(hand)==0:
            print 'Total score: ', acc, ' points'
            b=False
        else:
            print 'Current hand: ', 
            displayHand(hand)
            s=compChooseWord(hand, wordList, n)
            if(isValidWord(s,hand,wordList)):
                acc+=getWordScore(s,n)
                print '"',s,'"', ' earned ',getWordScore(s,n),' points. Total: ', acc, ' points'
                print ""
                hand = updateHand(hand,s)
            else:
                print 'Total score: ', acc, ' points'
                b=False
