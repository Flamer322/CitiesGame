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