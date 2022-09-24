from random import randint
import winsound
from time import sleep
import os


def clear():
    os.system('cls')


inv = {"Топор": 0, "Трофей": 0}


def death():
    clear()
    sleep(1)
    if input("Ты умер, начать сначала? Да/Нет\n>>").lower() == "да":
        start()
    else:
        exit()


def panik(inv):
    clear()
    if randint(0, 1):
        print("Ты находишь ржавый топор, паника помогла! Ты начинаешь осматриваться и идешь дальше")
        sleep(2)
        inv["Топор"] = 1
        challenge(inv)
    else:
        print("Ты натыкаешься на змею, она тебя кусает и ты погибаешь.")
        sleep(3)
        death()


def start():
    inNum = 1
    while not (inNum in {"1", "2", "3", "4"}):
        clear()
        inNum = (input("""Ты просыпаешься.
Все что ты знал о современном мире исчезло, люди вокруг обратились в камень.
Твои действия:
1. Паниковать
2. Паниковать.
3. ПАНИКОВАТЬ
4. Осмотреть местность
>> """))
        if inNum in {"1", "2", "3"}:
            panik(inv)
        elif inNum == "4":
            sleep(3)
            challenge(inv)
        else:
            print("Неправильно, попробуй еще раз")


def challenge(inv):
    clear()
    flag = 1
    if not randint(0, 4):
        print("Ты натыкаешься на группу выживших")
        sleep(3)
        survivers(inv)
    else:
        if inv["Топор"]:
            sleep(3)
            while flag:
                ans = input("Ты зарубил змею, будешь собирать труп? Да/Нет\n").lower()
                if ans == "да":
                    print("Ты подобрал труп змеи и пошел дальше")
                    sleep(3)
                    inv["Трофей"] = 1
                    survivers(inv)
                    flag = 0
                elif ans == "нет":
                    print("Ты пошел дальше")
                    sleep(3)
                    survivers(inv)
                    flag = 0
                else:
                    print("Неправильно, попробуй еще раз")
        else:
            print("Ты натыкаешься на змею, она тебя кусает и ты погибаешь.")
            sleep(3)
            death()


def survivers(inv):
    clear()
    if inv["Трофей"]:
        print("Выжившие встретили тебя как неплохого охотника, ты держал в руках труп ценной в этих кругах змеи.")
        sleep(3)
        win()
    else:
        print("Выжившие тебя не приняли и ты не смог найти себе пропитание в этом враждебном к слабым мире.")
        sleep(3)
        death()


def win():
    clear()
    print("Ты смог выжить в этом непростом квесте")
    winsound.PlaySound("victory_sJDDywi.wav", winsound.SND_ASYNC)
    sleep(10)


start()
