from random import randint


def displayIntro():
    print(
        """
_______________________________________________
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
_______________________________________________
_____________________Rules_____________________
Try to guess the hidden word one letter at a   
time. The number of dashes are equivalent to   
the number of letters in the word. If a player 
suggests a letter that occurs in the word,     
blank places containing this character will be 
filled with that letter. If the word does not  
contain the suggested letter, one new element  
of a hangman’s gallow is painted. As the game  
progresses, a segment of a victim is added for 
every suggested letter not in the word. Goal is
to guess the word before the man hangs!        
_______________________________________________

        """
    )


def displayEnd(result):
    if result == False:
        print(
            """
     __     __           _           _   _                                    
     \ \   / /          | |         | | | |                                   
      \ \_/ /__  _   _  | | ___  ___| |_| |                                   
       \   / _ \| | | | | |/ _ \/ __| __| |                                   
        | | (_) | |_| | | | (_) \__ \ |_|_|                                   
        |_|\___/ \__,_| |_|\___/|___/\__(_)                                   
            _______ _                                        _ _          _ _ 
           |__   __| |                                      | (_)        | | |
              | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |
              | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |
              | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|
              |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)
    __________________________________________________________________________
    
            """
        )
    else:
        print(
            """
    ________________________________________________________________________
              _                                  _                          
             (_)                                (_)                         
    __      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    
    \ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   
     \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      
      \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      
               | |   (_)    | |                  | (_)                      
            ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ 
           / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|
          | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   
           \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   
    ________________________________________________________________________
    
            """
        )


def displayHangman(state):
    hangmanStages = [
        """
         ._______.   
         |/          
         |           
         |           
         |           
         |           
         |           
     ____|___        

        """,
        """
         ._______.   
         |/      |   
         |           
         |           
         |           
         |           
         |           
     ____|___        
        """,
        """
         ._______.   
         |/      |   
         |      (_)  
         |           
         |           
         |           
         |           
     ____|___        

        """,
        """
         ._______.   
         |/      |   
         |      (_)  
         |       |   
         |       |   
         |           
         |           
     ____|___        
        """,
        """
         ._______.   
         |/      |   
         |      (_)  
         |      \|/  
         |       |   
         |           
         |           
     ____|___        
        """,
        """
         ._______.   
         |/      |   
         |      (_)  
         |      \|/  
         |       |   
         |      / \  
         |           
     ____|___        
        """
    ]

    print(hangmanStages[5 - state])


def getWord():
    with open('hangman-words.txt', 'r') as infile:
        data = infile.read()
    wordsAsList = data.splitlines()
    randWordIndex = randint(0, len(wordsAsList) - 1)
    randWord = wordsAsList[
        randWordIndex]  # we could use random.choice though, but as only randInt is imported I'm using that :)
    return randWord


def valid(c):
    if 97 <= ord(c) <= 122:
        return True
    return False


def play():
    word = getWord()
    unidentified_word = "".rjust(len(word), '*')  # filling with stars

    already_guessed_letters = []

    lives = 5
    result = False

    while lives >= 0:
        displayHangman(lives)

        if lives == 0:
            break

        print("Guess the word: " + unidentified_word)
        guess = input("Enter the letter: ")
        while not valid(guess):
            guess = input("Enter the letter: ")

        if word.find(guess) == -1:
            lives -= 1

        elif already_guessed_letters.count(guess) == 0:
            already_guessed_letters.append(guess)
            unidentified_word = word

            for letter in unidentified_word:
                if already_guessed_letters.count(letter) == 0:
                    unidentified_word = unidentified_word.replace(letter, '*')

            if unidentified_word == word:
                result = True
                break

    print("Hidden word was: " + word)

    return result


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        YesOrNo = input("Do you want to play again? (yes/no) ")
        if YesOrNo == "no":
            break


if __name__ == "__main__":
    hangman()
