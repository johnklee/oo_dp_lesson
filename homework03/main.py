#!/usr/bin/env python
class Meal:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def __str__(self):
        return f'{self.name} ({self.price})'


class FriedChicken(Meal):
    def __init__(self):
        super().__init__('炸雞', 50)


class Hambuger(Meal):
    def __init__(self):
        super().__init__('漢堡', 30)


class AbstractSideDish(Meal):
    def __init__(self, main_meal, drink, snack, extra_price):
        self.main_meal = main_meal
        self.drink = drink
        self.snack = snack
        super().__init__(
            f"{main_meal.name}|{self.drink}|{self.snack}",   # name
            main_meal.price + extra_price                    # price
        )


class SideDish1(AbstractSideDish):
    def __init__(self, main_meal):
        super().__init__(main_meal, '可樂', '薯條', 30)


class SideDish2(AbstractSideDish):
    def __init__(self, main_meal):
        super().__init__(main_meal, '紅茶', '雞塊', 60)


if __name__ == '__main__':
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
