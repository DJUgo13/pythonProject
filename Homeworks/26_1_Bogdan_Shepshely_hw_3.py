class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu * self.__memory

    def __str__(self):
        return f'Cpu: {self.__cpu}, Memory: {self.__memory}, Computation: {self.make_computations()}'

    def __eq__(self, other):
        return self.__memory == other


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - Beeline')

    def __str__(self):
        return f'Sim cards: {self.sim_cards_list}'


Phone.sim_cards_list = ['Beeline, Megacom, O']


class SmartPhone(Phone, Computer):
    def __init__(self, cpu, memory, sim_card_list, location):
        Phone.__init__(self, sim_card_list)
        Computer.__init__(self, cpu, memory)
        self.location = location

    def use_gps(self, location):
        print(f'Маршрут построен от вашего место положения до {location}')

    def __str__(self):
        return f'место куда вы проложили маршрут: {self.location}'


dell_inspiron = Computer(8, 512)
phone = Phone(1).call(1, 996557588777)
smart1 = SmartPhone(8, 64, 2, 'France')
smart2 = SmartPhone(32, 1000, 3, 'England')

print(dell_inspiron)
print(phone)
print(smart1)
print(smart2)

print(smart1.use_gps('GeekTech'))
print(dell_inspiron == smart1)

