def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    mystr = []
    for x in string.ascii_lowercase:
      if(x not in lettersGuessed):
       mystr.append(x)
    mystr = "".join(mystr)
    return mystr
