#!/usr/bin/env python
import abc



class Meal():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return f"{self.name}"
    
    def get_price(self) -> int:
        return f"{self.price}"

    def __str__(self):
        return f"{self.name} {self.price}"


class AbstractSideDish(Meal):
    def __init__(self, meal:Meal, drink, snack, combo_price):
        self.main_meal = meal
        self.drink = drink
        self.snack = snack
        self.combo_price = combo_price

    def get_name(self,) -> str:
        return f"{self.main_meal.get_name()}{self.drink}{self.snack}"

    def get_price(self) -> int:
        return f"{self.combo_price}"

    def __str__(self):
        return f"{self.main_meal.get_name()}{self.drink}{self.snack}{self.combo_price}"


class FriedChicken(Meal):
    def __init__(self, name = "炸雞", price = 50):
        self.name = name
        self.price = price

class Hambuger(Meal):
    def __init__(self, name = "漢堡", price = 30):
        self.name = name
        self.price = price
         
class SideDish1(AbstractSideDish):
    def __init__(self, main_meal, drink = "可樂", snack = "薯條", combo_price = 80):
        self.main_meal = main_meal
        self.drink = drink
        self.snack = snack
        self.combo_price = combo_price

class SideDish2(AbstractSideDish):
    def __init__(self, main_meal, drink = "紅茶", snack = "雞塊", combo_price = 90):
        self.main_meal = main_meal
        self.drink = drink
        self.snack = snack
        self.combo_price = combo_price

 

if __name__ == '__main__':
    # 只點主餐
    fc = FriedChicken()
    hb = Hambuger()
    print(fc)               # 預期看到 "炸雞 (50)"
    print(fc.get_name())    # 預期看到 "炸雞"
    print(fc.get_price())   # 預期看到 50
    print(hb)               # 預期看到 "漢堡 (30)"
    print(hb.get_name())    # 預期看到 "漢堡"
    print(hb.get_price())   # 預期看到 30

    # 點 主餐 + 附餐
    sd1 = SideDish1(fc)
    sd2 = SideDish2(hb)

    print(sd1)              # 預期看到 "炸雞|可樂|薯條 (80)"
    print(sd1.drink)        # 預期看到 "可樂"
    print(sd1.snack)        # 預期看到 "薯條"
    print(sd1.main_meal)    # 預期看到 "炸雞 (50)"
    print(sd1.get_name())   # 預期看到 "炸雞|可樂|薯條
    print(sd1.get_price())  # 預期看到 80

    print(sd2)              # 預期看到 "漢堡|紅茶|雞塊 (90)"
    print(sd2.drink)        # 預期看到 "紅茶"
    print(sd2.snack)        # 預期看到 "雞塊"
    print(sd2.main_meal)    # 預期看到 "漢堡 (30)"
    print(sd2.get_name())   # 預期看到 "漢堡|紅茶|雞塊
    print(sd2.get_price())  # 預期看到 90

    sd1 = SideDish1(hb)
    print(sd1)              # 預期看到 ?
    print(sd1.drink)        # 預期看到 ?
    print(sd1.snack)        # 預期看到 ?
    print(sd1.get_name())   # 預期看到 ?
    print(sd1.get_price())  # 預期看到 ?

