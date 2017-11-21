

def fixString(sentence):
    cutWords = [' the ', ' at ', ' to ', ' with ', ' the ', ' on ', ' like ']
    """
    Fix string allows the System to better understand user arguments.
    ____>>>>Iteration One: Eliminates whitespace.
    Iteration Two: Eliminates punctuation
    Iteration Three:
    :param sentence:
    :return:
    """
    ### The next iteration will remove punctuation.
    sentence = sentence.lower()
    for word in cutWords:
        if word in sentence:
            sentence = sentence.replace(word, " ")
    sentence = sentence.replace(" ", "")
    return sentence


def addIT(word):
    word = word + '  5'
    word = fixString(word)
    print(word)

#addIT('can I see what that the mouth do though to for eight dollars')



def testTheWord(word):
    """
    Will check if the word is in the string better than an array loop comparison via built-in function.
    :param word:
    :return:
    ### currently prints if the word is there. Next step is to integrate this into Synonym Engine
    """
    # begin by killing all whitespace
    word = fixString(word)
    print(word)
    # integrate logic of an array
    for rand in randomwords:
        if rand in word:
            print("that one is there")
        else:
            print('that one was not there')


#testTheWord("King's landing")

