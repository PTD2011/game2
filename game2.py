import random
import time

class player:

    def __init__(self):
        self.healPoints = 100
        self.attackPoints = 10
        self.superAttackPoints = 15
        self.defeancePoints = 25
    
    def attack(self):
        print('Вы атаковали')
        return  self.attackPoints
#лёгкие мобы

class spider:
    def __init__(self):
        self.healPoints = 30
        self.attackPoints = 8 
    
    def attack(self):
        print('Вас атаковал паук')
        return self.attackPoints


class skelet:
    def __init__(self):
        self.healPoints = 25
        self.attackPoints = 6

    def attack(self):
        print('Вас атаковал скелет')
        return self.attackPoints


#средние мобы


class darkPrince:
    def __init__(self):
        self.healPoints = 60
        self.attackPoints = 20
        self.defeancePoints = 0

    def attack(self):
        print('На вас напал тёмный принц')
        return self.attackPoints
    
    

class slime:
    def __init__(self):
        self.healPoints = 50
        self.attackPoints = 15

    def attack(self):
        print('На вас напал слайм')
        return self.attackPoints

#тяжёлые мобы

class cyclope:
    def __init__(self):
        self.healPoints = 80
        self.attackPoints = 35
        self.defeancePoints = 29

    def attack(self):
        print('На вас напал цыклоп')
        return self.attackPoints

class kingSnake:
    def __init__(self):
        self.healPoints = 95
        self.attackPoints = 49

    def attack(self):
        print('На вас напал король змей')
        return self.attackPoints

#босс

class Boss:
    def __init__(self):
        self.healPoints = 115
        self.attackPoints = 65

    def attack(self):
        print('На вас напал БОСС')
        return self.attackPoints

def greetings():
    print('Добро пожаловать в игру! By PTD\n\n\n\n\tЖил да был народ никого не трогал')
    print('\tи был у них священный огонь, что грел их, но однажды...\n\tПришел Рог и забрал его')
    print('\tна самую высокую гору\n\tНо был в этом народе герой который пошел ')
    print('\tзабирать его обратно и с этого момента его история началась.')
    print('\n\tШёл наш герой и увидел проход в горе вошел в него и встретил там приспешников Рога')
    print('\n\tИ началась битва!!!!')
    print('\n\n\t\tПравилa')
    print('\tУ вас будет 2 секунды на выбор действий, и если вы выбрали уклон то вам предстоит за 2 секунды ввести')
    print('\tчисло, которое резко появится на экране, если вы не успеете его ввести, или введете не то число, то')
    print('\tсчитается что вы не смогли уклониться и получили урон.')

def mobAttack(mobObject, userObject):
    mobAttackPoints = mobObject.attack()
    startTimer = time.time()
    isReady = input('a - щит, z - уклон')
    endTimer = time.time()

    if endTimer - startTimer > 2:
        print('Вы не успели')
        userObject.healPoints -= mobAttackPoints

    else:
        if isReady == 'a' and userObject.defeancePoints > 0:
            userObject.defeancePoints -= mobAttackPoints
        elif userObject.defeancePoints <= 0 and isReady == 'a':
            print('Твой щит разбился больше ты не сможешь защититься от удара.')

        elif isReady == 'z':
            randomValue = random.randint(10, 999)
            print(randomValue)
            startTimer = time.time()
            userAns = int(input('Введите число:', )
            endTimer = time.time()
            
            if endTimer - startTimer > 3 or userAns != randomValue:
                print('Вы не успели увернуться.')
                userObject.healPoints -= mobAttackPoints
            elif endTimer - startTimer <= 3 and userAns == randomValue:
                print('Вы успели увернуться.')
                
            

                
def userAttack(userObject, mobObject):
    userAttackPoints = userObject.attack()
    #есть рандомный пример = randExpressionAns
    print(randExpressionAns)
    startTimer = time.time()
    userAns = int(input('Введите ответ:', )
    endTimer = time.time()
    if endTimer - startTimer > 5 or userAns != randExpressionAns:
        print('Вы промахнулись.')
    elif endTimer - startTimer <= 5 and userAns == randExpressionAns:
        print('Вы попали.')
        mobObject -= userObject.attack()

