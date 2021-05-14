#Python program for Lucky Draw Game
import os
import time

def main():
    os.system('cls')
    print("\t\tLUCKY DRAW!!!! \n\n")
    print("Instruction:\nThe computer will select a random number between 1 to 10.")
    print("You are supposed to guess the number. If correct you'll recieve 5 points\n")
    p=0
    ch='y'
    while ch=='y'or ch=='Y':
        d=int(input("Enter your number(1-10):"))
        import random
        r=random.randint(0,10)
        if d==r:
            p+=5
            print("\nYour number was the lucky number!!!! Congratulations, you've earned 5 points!!")
        else:
            print("\nOops, that wasn't the lucky number(!-!)")
        ch=input("Do you want to continue playing(y/n): ")
        ch.lower()
    print("\n\nYour total score is %d \n\n\t\t Thank you for playing!!!" %p)
    time.sleep(1)

if __name__ == "__main__":
    main()
    