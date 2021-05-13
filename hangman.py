import random

def wordsrack():
    list_of_words=("nandanunni","computer","ramapuram","beefbiryani")
    return random.choice(list_of_words)

def guessword():
    word = wordsrack()
    ln = len(word)
    letters=[]
    k=0
    i=0
    newword=[]
    for i in range(ln):
        if i == 0 or i==3 or i==4 or i==6 or i==7:
            newword.append("_")
            letters.insert(i,word[i])
            k=k+1
        else:
            newword.insert(i,word[i])
    return word,newword,letters,ln

def comparer(word,new):
    i=0
    l=len(word)
    for i in range(l):
        if(word[i]!=new[i]):
            return False
        
def thegame():
    w,nw,l,ln=guessword()
    life = 4
    points=0
    print("\nYour word is : %s"%nw)
    while life > 0:
        status = False
        i=0
        j=0
        if comparer(w,nw)==0:
            g=input("Enter your guess :")

        for j in range (5):
            if (l[j] == g):
                status = True
                l[j]=j

        if (status == True ):
            for i in range (ln):
                if(w[i] == g):
                    nw[i] = g

            print("Right guess!!")
            if comparer(w,nw)==0:
                print("\nyour word : %s"%nw)
                print ("you have %d life left !"%life)
                print("\n")
            else:
                print("\nCongrats you've guessed the word correctly!! ")
                print("Your word was %s"%w)
                print("You guessed with %d lives left"%life)
                points=5
                break
        else:
            life=life-1
            if comparer(w,nw)==0:
               print("Wrong guess!!")
               print("\nYour word : %s"%nw)
               print("you have %d lives left"%life)
               print("\n")
        if(life==0):
            print("Game over!!")
            print("your word was %s"%w)
            points=-5
    return points


print("__________HANGMAN GAME__________\n")
name=input("Enter your name:")
print("\n\nYou are given a word with some missing letters,you are supposed to guess every letter in that word.\nYou are given 4 lives for mistakes. \nGuess the word before you DIE.....HAHA\n")
print("Ps:you'll recieve points for each round you win....\n\n")
c='y'
points=0
while c=='y' :
    points=points+thegame()
    print("\n\nYou're totalpoints:%d"%points)
    c=input("\nDo you want to play again : (y/n)")
    c.lower()
