import random
import os
import time

def title():
    os.system('cls')
    print("\t\tTrivia Quiz\n\n")
    print("Instruction:\nThere are 2 difficulties with each one having 5 questions.")
    print("\nYou'll recieve points for each correct answer")
    pause()

def pause():
    input("\n\tPress enter to continue..")

def easydiff():
    points=0
    qn=0
    r=random.sample(range(10),5)
    quiz={
        0:{'Question':'What is the rarest blood type?',
        'Answer':'ab negative'},
        1:{'Question':'How many bones are there in the human body?',
        'Answer':'206'},
        2:{'Question':'What is the name of the musical artist who sings the song Watermelon Sugar?',
        'Answer':'harry styles'},
        3:{'Question':' What does Na stand for on the periodic table?',
        'Answer':'sodium'},
        4:{'Question':'Which planet is closest to Earth?',
        'Answer':'venus'},
        5:{'Question':'Who is the author of the Harry Potter series?',
        'Answer':'j k rowling'},
        6:{'Question':'What temperature (in Fahrenheit) does water freeze at?',
        'Answer':'32'},
        7:{'Question':'Typewriter is the longest word that can be typed using only the first row on a QWERTY keyboard.(True/False)',
        'Answer':'true'},
        8:{'Question':'A doctor with a PhD is a doctor of what?',
        'Answer':'philosophy'},
        9:{'Question':' How many Harry Potter books are there?',
        'Answer':'7'}
    }
    print("....")
    while(qn<5):
        ra=r[qn]
        print("\n")
        print(quiz[ra]['Question'])
        guess=input("\t:")
        guess=guess.lower()
        print("\n")
        ans=quiz[ra]['Answer']
        if(ans==guess):
            print("correct answer")
            points=points+5
        else:
            print("wrong answer")
            print("correct answer was :%s"%ans)
        qn=qn+1
    print("You have recieved %d points"%points)
    return points

def harddiff():
    print("Test")
    points=0
    qn=0
    r=random.sample(range(10),5)
    quiz={
        0:{'Question':'Where is the Great Barrier Reef located?',
        'Answer':'australia'},
        1:{'Question':'What country saw a world record 315 million voters turn out for elections on May 20, 1991?',
        'Answer':'india'},
        2:{'Question':'When did the website "Facebook" launch?',
        'Answer':'2004'},
        3:{'Question':'What is the worlds best-selling book? ',
        'Answer':'bible'},
        4:{'Question':'What language is the most popularly spoken worldwide?',
        'Answer':'chinese'},
        5:{'Question':'What is the name of Shakespeare’s shortest tragedy?',
        'Answer':'macbeth'},
        6:{'Question':'What color is the M in McDonald’s?',
        'Answer':'yellow'},
        7:{'Question':'Which is the only edible food that never goes bad?',
        'Answer':'honey'},
        8:{'Question':'Which country invented ice cream?',
        'Answer':'china'},
        9:{'Question':'Which Former NBA Player Was Nicknamed “Agent Zero”?',
        'Answer':'gilbert arenas'}
    }
    print("....")
    while(qn<5):
        ra=r[qn]
        print("\n")
        print(quiz[ra]['Question'])
        guess=input("\t:")
        guess=guess.lower()
        print("\n")
        ans=quiz[ra]['Answer']
        if(ans==guess):
            print("correct answer")
            points=points+5
        else:
            print("wrong answer")
            print("correct answer was %s"%ans)
        qn=qn+1
    print("You have recieved %d points"%points)
    return points

def main():
    title()
    diff=0
    ch='y'
    points=0
    while(ch=='y'):
         diff=int(input("\n\nDifficulties available: \n1.Easy\n2.Medium\n\nYour choice: "))
         if(diff==1):
             points=points+easydiff()
         else:
             points=points+harddiff()
         ch=input("Do you want to play again: ")
         ch=ch.lower()
    print("\n\nYour total score is %d points"%points)
    time.sleep(1)
    

if __name__ == "__main__":
    main()