from os import system
import math
tried = []#dict()
misses = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
word = input("Player 1, enter your word: ")

def getDisplayWord():
    dw = word
    for letter in word:
        if letter not in tried:
            dw = dw.replace(letter, "_")
    return dw

def getMisses():
    lst = []
    for letter in tried:
        if letter not in word:
            lst.append(letter)
    return lst

def checkWin():
    for letter in word:
        if letter not in tried: return False
    return True

#from stackoverflow: CrouZ
def waitForKey():
    #if system == "Windows":
    system("pause")
    #else:
    #    system("/bin/bash -c 'read -s -n 1 -p \"Press any key to continue...\"'")
    #print()

lives = math.max(3, 8 - int(math.sqrt(len(word))))
msg = ""
while lives > 0:
    #clear terminal and output game info
    system("cls")
    print(getDisplayWord())
    print(f"chances left: {lives}")
    if len(misses) > 0: print(f"misses: {misses}")
    guess = input(f"Player 2, enter your guess: \n{msg}\n")

    if len(guess) != 1:
        msg = "Please enter a single letter."
    elif guess in tried:
        msg = f"You already guessed '{guess}'."
    else:
        tried.append(guess)
        if guess in word:
            msg = f"'{guess}' is in Player 1's word!"
            if checkWin(): 
                # win
                print(f"Player 1 has completed the word: '{word}'!")
                #waitForKey()
                exit()
        else:
            msg = f"'{guess}' is not in Player 1's word."
            lives -= 1
            misses.append(guess)
    #waitForKey()
# loss
print(f"Player 2 falied to guess: '{word}' - Player 1 wins!")