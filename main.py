from random import randint

inv = dict() 

def death():
    print("Ты умер")

def panik(inv):
    if randint(1, 4) == 1:
        print("Ты находишь ржавый топор, паника помогла!")
        inv["Топор"] = 1
        survivers()
    else:
        death()

def start():
    inNum = int(input("""Ты просыпаешься.
Все что ты знал о современном мире исчезло, люди вокруг обратились в камень.
Твои действия:
1. Паниковать
2. Паниковать.
3. ПАНИКОВАТЬ
4. Осмотреть местность
>> """))
    if inNum in {1, 2, 3}:
        panik()
    else:
        death()
    if inNum == 4:
        survivers()
def challenge(inv):
    if randint(0, 1):
        print("Ты натыкаешься на группу выживших")
        survivers(inv)
    else:
        if inv["Топор"]:
            print("Ты зарубил змею, будешь ")
        print("Ты натыкаешься на змею, она тебя кусает и ты погибаешь.")
    
