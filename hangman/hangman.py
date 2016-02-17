def getguessedWord(secretWord, lettersGuessed):
    mystr = []   
    for x in secretWord:
      if(x in lettersGuessed):
         mystr.append(x)
      else:      
         mystr.append('_')
    mystr = "".join(mystr)
    return mystr
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game Hangman!"
    ct=8
    chr=''
    a=[]
    b=[]
    remainWord = secretWord
    curWord = ''
    print "I am thinking of a word that is ", len(secretWord)," letters long."
    while (ct!=0):
        print "-----------"
        print "You have ",ct," guesses left."
        print "Available Letters: ", getAvailableLetters(a)
        CHR = raw_input("Please guess a letter: ")
        chr = CHR.lower()
        if (chr not in a):
            a.append(chr)
            if( chr in secretWord):
                b.append(chr)
                remainWord = getguessedWord(secretWord,b) 
                print "Good guess: ",remainWord    
            else:  
                ct-=1
                remainWord = getguessedWord(remainWord,chr) 
                print "Oops! That letter is not in my word: ", remainWord
        else: 
            print "Oops! You've already guessed that letter: ",remainWord   
        if(isWordGuessed(remainWord,a)):
            ct=0
    print "-----------"
    if(isWordGuessed(remainWord,a)):
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses. The word was else."