import time
import random


class Fighter:
    def __init__(self, name, surname, win_by_knock, win_by_sub, win_by_dec):
        self.name = name
        self.surname = surname
        self.win_by_knock = win_by_knock
        self.win_by_sub = win_by_sub
        self.win_by_dec = win_by_dec

    def create_list_name_surname(self):
        list_of_name = [self.name + " " + self.surname]
        return list_of_name[0]

    def create_list_of_chance(self):
        list_of_chance = [self.win_by_knock, self.win_by_sub, self.win_by_dec]
        return list_of_chance

    def sum_of_chance(self):
        sum_chance = (self.win_by_knock, self.win_by_sub, self.win_by_dec)
        return int(sum(sum_chance))


def create_new_fighter():
    name = input("Podaj imie: ")
    surname = input("Podaj nazwisko: ")
    win_by_knock = int(input("Podaj szansę na nokaut: "))
    win_by_sub = int(input("Podaj szansę na poddanie: "))
    win_by_dec = int(input("Podaj szansę na decyzję: "))
    fighterData = Fighter(name, surname, win_by_knock, win_by_sub, win_by_dec)
    return fighterData


def pick_random_win(list_chance):
    type_of_win = ["Knockout", "Submission", "Decision"]
    return random.choices(type_of_win, list_chance)[0]


def pick_one_and_remove(list_of_fighters):
    randomFighter = random.choice(list_of_fighters)
    list_of_fighters.remove(randomFighter)
    return randomFighter


def random_minute_second_of_round():
    x = int(random.uniform(0, 60))
    y = int(random.uniform(0, 5))
    if x <= 9:
        return str(y) + ":" + "0" + str(x)
    else:
        return str(y) + ":" + str(x)


def random_round():
    rounds = ("First", "Second", "Third", "Fourth", "Fifth")
    one_round = random.choice(rounds)
    return one_round.upper()


def random_category_weight():
    list_of_category = ["Heavyweight", "Light heavyweight", "Middleweight",
                        "Welterweight", "Lightweight", "Featherweight", "Bantamweight"]
    one_of_them = random.choice(list_of_category)
    return one_of_them.upper()


def random_type_of_win_by_dec():
    types = ["Split", "unanimous", "Majority"]
    picking = random.choice(types)
    return picking.upper()


first_fighter = create_new_fighter()
print("\n")
second_fighter = create_new_fighter()
print("\n")
third_fighter = create_new_fighter()
print("\n")
fourth_fighter = create_new_fighter()
print("\n")
list_of_fighters = [first_fighter,
                    second_fighter, third_fighter, fourth_fighter]

first_fighter = pick_one_and_remove(list_of_fighters)
second_fighter = pick_one_and_remove(list_of_fighters)
third_fighter = pick_one_and_remove(list_of_fighters)
fourth_fighter = pick_one_and_remove(list_of_fighters)

# first round
print("First Battle", first_fighter.create_list_name_surname().upper(), "VS",
      second_fighter.create_list_name_surname().upper())
twoFighters = (first_fighter, second_fighter)
x = first_fighter.sum_of_chance()
y = second_fighter.sum_of_chance()
xy = [x, y]
first_fighter = random.choices(twoFighters, xy)
first_fighter = first_fighter[0]
time.sleep(3)
print("\n")
print("Winner from first fight is...")
time.sleep(4)
print("\n")
print(first_fighter.create_list_name_surname().upper())
x = pick_random_win(first_fighter.create_list_of_chance()).upper()
time.sleep(3)
if x == "DECISION":
    print("Won By", random_type_of_win_by_dec(), x)
    time.sleep(3)
else:
    print("Won By", x)
    time.sleep(2)
    print("At", random_minute_second_of_round(), "of", random_round(), "round")
    time.sleep(2)
print("-"*40)
time.sleep(5)
# second round
print("Second Battle", third_fighter.create_list_name_surname().upper(), "VS",
      fourth_fighter.create_list_name_surname().upper())
time.sleep(3)
print("\n")
twoFighters = (third_fighter, fourth_fighter)
x = third_fighter.sum_of_chance()
y = fourth_fighter.sum_of_chance()
xy = [x, y]
second_fighter = random.choices(twoFighters, xy)
second_fighter = second_fighter[0]
print("Winner from second fight is...")
time.sleep(4)
print("\n")
print(second_fighter.create_list_name_surname().upper())
x = pick_random_win(second_fighter.create_list_of_chance()).upper()
time.sleep(3)
if x == "DECISION":
    print("Won By", random_type_of_win_by_dec(), x)
    time.sleep(3)
else:
    print("Won By", x)
    time.sleep(2)
    print("At", random_minute_second_of_round(), "of", random_round(), "round")
    time.sleep(3)
print("-"*40)

# main event
print("MAIN EVENT")
time.sleep(3)
print("\n")
print("Battle about Title Champion at", random_category_weight(), "division")
time.sleep(3)
print("\n")
print("Fight between", first_fighter.create_list_name_surname().upper(), "and",
      second_fighter.create_list_name_surname().upper())
time.sleep(4)
print("\n")
x = first_fighter.sum_of_chance()
y = second_fighter.sum_of_chance()
xy = [x, y]
winner = (first_fighter, second_fighter)
winner = random.choices(winner, xy)
winner = winner[0]
print("The winner is...")
time.sleep(4)
print("\n")
print(winner.create_list_name_surname().upper())
time.sleep(3)
x = pick_random_win(winner.create_list_of_chance()).upper()
if x == "DECISION":
    print("Won By", random_type_of_win_by_dec(), x)
else:
    print("Won By", x)
    time.sleep(2)
    print("At", random_minute_second_of_round(), "of", random_round(), "round")
time.sleep(20)
