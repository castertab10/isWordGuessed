def isWordGuessed():

    secretWord = input("Input the secret word: ")
    lettersGuessed = input("Input a list of letters: ")
    n = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            n += 1
        else:
            return False
    return True
    
    
    
#    secretWord = input("input the secret word: ")
#    n = input("input a list of letters separated by spaces: ")
#    lettersGuessed = n.split()
    
#    print(m, lettersGuessed)
   
#    if m == lettersGuessed:
 #       print("True")
 #   else:
 #       print("False")