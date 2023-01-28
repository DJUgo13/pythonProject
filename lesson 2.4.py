import random
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4
    SIZE_ON = 5
    REVIVE = 6
    REVERT_HEALTH = 7
    BOOM = 8
    POISON_BLADE = 9


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        selected_hero = random.choice(heroes)
        self.__defence = selected_hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health = hero.health - self.damage

    def __str__(self):
        return "BOSS " + super(Boss, self).__str__() + f" defence: {self.__defence}"


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super(Hero, self).__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        if boss.health > 0 and self.health > 0 and self.__super_ability != boss.defence:
            boss.health = boss.health - self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = random.randint(2, 5)
        print(f"Coefficient of Critical: {coeff}")
        boss.health -= self.damage * coeff


class Magic(Hero):
    def __init__(self, name, health, damage):
        super(Magic, self).__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        boost_points = random.randint(5, 11)
        print(f"Boost: {boost_points}")
        for hero in heroes:
            if hero != self and hero.health > 0 and hero.super_ability != SuperAbility.CRITICAL_DAMAGE:
                hero.damage += boost_points


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super(Medic, self).__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if self != hero and hero.health > 0:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super(Berserk, self).__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0


class AntMan(Hero):
    def __init__(self, name, health, damage):
        super(AntMan, self).__init__(name, health, damage, SuperAbility.SIZE_ON)

    def apply_super_power(self, boss, heroes):
        rnd = random.randint(1, 5)
        if rnd == 5:
            self.health += 150
            self.damage += 8
            print("+ Size")
        elif rnd == 1 or 2 or 3 or 4:
            self.health -= 150
            self.damage -= 3
            print(" - Size")


class Wither(Hero):
    def __init__(self, name, health, damage):
        super(Wither, self).__init__(name, health, damage, SuperAbility.REVIVE)

    def apply_super_ability(self, heroes):
        self.damage = 0
        for hero in heroes:
            if hero.health >= 0:
                self.health = hero.health


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super(Hacker, self).__init__(name, health, damage, SuperAbility.REVERT_HEALTH)

    def apply_super_power(self, boss, heroes):
        hp = random.randint(10, 21)
        print(f'hp of revert: {hp}')
        for hero in heroes:
            boss.health -= hp
            hero.health += hp


class Bomber(Hero):
    def __init__(self, name, health, damage):
        super(Bomber, self).__init__(name, health, damage, SuperAbility.BOOM)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if self.health == 0:
                self.damage = 100
                print(f'Bomber die and give damage: {self.damage}')
            else:
                hero.health = hero.health - self.damage


class Assassin(Hero):
    def __init__(self, name, health, damage):
        super(Assassin, self).__init__(name, health, damage, SuperAbility.POISON_BLADE)

    def apply_super_power(self, boss, heroes):
        blade = random.randint(1, 5)
        if blade == 1:
            self.damage += 10
            print(f'Assassin use poison blade and give damage: {self.damage}')

# класс ассасин - способность данного класса в том что при атаке рандомно выбирается каким клинком наносить атаку.
# при атаке отравленым клинком яд в теле босса накапливается так же как и дамаг нанесенный боссу


round_number = 0


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!!!")
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss won!!!")
    return all_heroes_dead


def print_statistics(boss, heroes):
    print("ROUND " + str(round_number) + " -----------------")
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if hero.health > 0 and hero.super_ability != boss.defence:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss("Rashan", 2000, 70)
    warrior = Warrior("Hunter", 270, 10)
    doc = Medic("Yor", 250, 5, 15)
    magic = Magic("Invoker", 280, 20)
    berserk = Berserk("Axe", 260, 15)
    assistant = Medic("Devi", 290, 10, 5)
    antman = AntMan('Bogdan', 300, 12)
    wither = Wither('Deiman', 290, 0)
    hacker = Hacker('Bill', 250, 14)
    bomber = Bomber('Big boom', 50, 16)
    assassin = Assassin('Phantom', 260, 15)

    heroes = [warrior, doc, magic, berserk, assistant, antman, wither, hacker, bomber, assassin]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()
print('alan')
