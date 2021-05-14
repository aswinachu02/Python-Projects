import os
import LuckyDraw
import Quiz
import hangman
import time

def main():
    def title():
        clear()
        print("\t\t_______Game Vault______\n\n")
    
    def clear():
        os.system('cls')

    def delay():
        time.sleep(1)

    status = True
    while(status!=False):
        title()      
        print("The available games are:")
        print("\n1.Hangman\n2.Luckydraw\n3.Quiz")
        ch=int(input("\n\nEnter your selection..\n\t\t:"))
        delay()
        if (ch==1):
            hangman.main()
        elif (ch==2):
            LuckyDraw.main()
        else:
            Quiz.main()
        title()
        c=input("Do you want to play another game?(y/n)\n\t\t:")
        c=c.lower()
        if c=='y':
            status=True
        else:
            status=False
    clear()
    print("\t\tThank you for visiting!!!!")
    delay()


if __name__ == "__main__":
    main()
        