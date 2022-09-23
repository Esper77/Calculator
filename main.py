from random import randint
import winsound
from time import sleep
inv = ["Топор":0, "Трофей":0]

def death():
    sleep(1)
    if lower(input("Ты умер, начать сначала?")) == "да":
        start()
    else:
        exit()

def panik(inv):
    if randint(1, 4) == 1:
        print("Ты находишь ржавый топор, паника помогла!")
        inv["Топор"] = 1
        survivers()
    else:
        print("Ты натыкаешься на змею, она тебя кусает и ты погибаешь.")
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
        challenge(inv)
    if inNum == 4:
        sleep(3)
        survivers()

def challenge(inv):
    if randint(0, 1):
        print("Ты натыкаешься на группу выживших")
        survivers(inv)
    else:
        if inv["Топор"]:
            if lower(input("Ты зарубил змею, будешь собирать труп? Да/Нет")) == "да":
                print("Ты подобрал труп змеи и пошел дальше")
                inv["Трофей"] = 1
            else:
                print("Ты пошел дальше")
        else:
            print("Ты натыкаешься на змею, она тебя кусает и ты погибаешь.")
            death()

def survivers(inv):
    if inv["Трофей"]:
        print("Выжившие встретили тебя как неплохого охотника, ты держал в руках труп ценной в их кругах змеи.")
        win()
    else:
        print("Выжившие тебя не приняли и ты не смог найти себе пропитание в этом враждебном к слабым мире.")
        death()

def win():
    print("Ты смог выжить в этом непростом квесте")
    winsound.PlaySound("victory_sJDDywi.wav", winsound.SND_ASYNC)
