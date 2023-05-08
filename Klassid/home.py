# Meil on inimene. Inimesel on:
# staatilised väljad nimi ja vanus
# ning dünaamilised väljad raha, kodu
# Inimene võib: anda enda kohta infot, 
# teenida raha, osta kodu
# Meil on Kodu. Kodu kohta meil on:
# pindala, hind
# Kodu ostmiseks võime saada allahindlust.


class Human:
    default_name = 'No_name'
    default_age = 35

    def __init__(self, money, house,
    name = default_name,
    age = default_age):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house
    
    def info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Money: ", self.__money)
        print("House: ", self.__house)

    def earn_money(self, amount):
        if isinstance(amount, (int, float)):
            self.__money = self.__money + amount
        else:
            print("Only accept number as the amount of earning")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def buy_house(self, house, discount = 0):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print("Not enough money for a deal")
        return

class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price
    
    def final_price(self, discount):
        final_price = self._price*(100-discount)/100
        return final_price

    def __str__(self):
        return "My house is " + str(self._area) + " square meters big."
    def __repr__(self):
        return "My house is" + str(self._area) + " square meters big."

house = House(40, 90000)
fedor = Human(0, None, 'Fedor', 32)
fedor.buy_house(house, 100)
fedor.info()
input()
