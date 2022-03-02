from abc import abstractmethod, ABC


class Cooker:
    def cook_beef(self):
        print("Beef is ready")
        return 'beef'

    def cook_chicken(self):
        print("Chicken is ready")
        return 'chicken'


class Command(ABC):
    def do(self):
        raise NotImplemented()


class CommandOrderBeef(Command):
    def __init__(self, cooker):
        self.cooker = cooker

    def do(self):
        return self.cooker.cook_beef()


class CommandOrderChicken(Command):
    def __init__(self, cooker):
        self.cooker = cooker

    def do(self):
        return self.cooker.cook_chicken()


class Waiter:
    def __init__(self):
        # Key as command name; value as command object
        self.cmd_dict = {}
        self.orders = []

    def give_order(self, order):
        self.orders.append(self.cmd_dict[order])

    def send_order(self):
        print("Send out order...")
        dish_list = []
        for o in self.orders:
            dish_list.append(o.do())

        self.orders = []
        return dish_list


class Restaurant:
    def __init__(self):
        self.waiter = Waiter()
        self.cooker = Cooker()
        self.waiter.cmd_dict['beef'] = CommandOrderBeef(self.cooker)
        self.waiter.cmd_dict['chicken'] = CommandOrderChicken(self.cooker)

    def start_business(self):
        self.waiter.give_order('beef')
        self.waiter.give_order('chicken')
        my_dish = self.waiter.send_order()
        return my_dish

    def start_business_with_new_dish(self):
        # TBD
        pass
