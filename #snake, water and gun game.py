#snake, water and gun game
import random
def gameWin(comp, you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='w':
            return True
        if you=='s':
            return False

print("Comp turn: Snake(s) Water(w) or Gun(g)?")
randNumber =random.randint(1, 3)

if randNumber==1:
    comp = 's'
elif randNumber==2:
    comp = 'w'
elif randNumber==3:
    comp = 'g'

you=input("Your turn: Snake(s) Water(w) or Gun(g)?")
a=gameWin(comp, you)
print(randNumber)
print(f"Computer chose {comp}")
print(f"You chose {you}")
if a== None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
