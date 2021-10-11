import time

class CitiesDict:
    def __init__(self):
        self.cities = {}
        with open('cities.txt', 'r', encoding='utf-8') as read_file:
            for city in read_file:
                city = city.lower()
                self.cities[city[:-1]] = True

    def is_city(self, city):
        city = city.lower()
        return city in self.cities

    def is_available(self, city):
        city = city.lower()
        return self.cities.get(city)

    def select_city(self, city):
        city = city.lower()
        if self.is_available(city):
            self.cities[city] = False
            return True
        else:
            return False

    def get_next_char(self, city):
        city = city.upper()
        if city[-1] in ['Ы', 'Й', 'Ь', 'Ъ']:
            return city[-2]
        else:
            return city[-1]


class Watch:
    def __init__(self, players):
        self.players = players
        self.turn_times = []
        self.turn = 0
        self.start_time = 0

    def next_turn(self, turn_time):
        self.turn += 1
        self.turn_times.append(turn_time)
        return self.turn

    def get_turn_time(self):
        turn_time = round(time.perf_counter() - self.start_time, 1)
        self.start_time = time.perf_counter()
        return turn_time

    def start_stopwatch(self):
        self.start_time = time.perf_counter()

    @property
    def turn_time(self):
        return 10 + self.turn / 10

    @property
    def average_turn_times(self):
        sum_time = []
        n = []
        avg_times = []
        for i in range(self.players):
            sum_time.append(0)
            n.append(0)
        for i in range(0, len(self.turn_times)):
            sum_time[i % self.players] += self.turn_times[i]
            n[i % self.players] += 1
        for i in range(0, self.players):
            if n[i] == 0:
                avg_times.append(0)
            else:
                avg_times.append(round(sum_time[i] / n[i], 1))
        return avg_times