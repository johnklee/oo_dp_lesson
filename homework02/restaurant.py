from abc import abstractmethod, ABC

class Cooker:
    def cookBeef(self):
        print("Beef is ready")
        return 'beef'

    def cookChicken(self):
        print("Chicken is ready")
        return 'chicken'

    def cookPork (self):
        print("Pork is ready")
        return 'pork'


class Command(ABC):
    def do(self):
        raise NotImplemented()


class CommandOrderBeef(Command):
    def __init__(self, cooker):
        self.cooker = cooker

    def do(self):
        return self.cooker.cookBeef()


class CommandOrderChicken(Command):
    def __init__(self, cooker):
        self.cooker = cooker

    def do(self):
        return self.cooker.cookChicken()

class CommandOrderPork(Command):
    def __init__(self, cooker):
        self.cooker = cooker

    def do(self):
        return self.cooker.cookPork()


class Waiter:
    def __init__(self):
        # Key as command name; value as command object
        self.cmd_dict = {}
        self.orders = []

    def giveOrder(self, order):
        self.orders.append(self.cmd_dict[order])

    def sendOrder(self):
        print("Send out order...")
        dish_list = []
        for o in self.orders:
            dish_list.append(o.do())

        self.orders = []
        return dish_list

'''
class Restaurant:
    def __init__(self):
        self.waiter = Waiter()
        self.cooker = Cooker()
        self.waiter.cmd_dict['beef'] = CommandOrderBeef(self.cooker)
        self.waiter.cmd_dict['chicken'] = CommandOrderChicken(self.cooker)
        self.waiter.cmd_dict['pork'] = CommandOrderPork(self.cooker)

    def start_business(self):
        self.waiter.giveOrder('beef')
        self.waiter.giveOrder('chicken')
        my_dish = self.waiter.sendOrder()
        return my_dish
    

    def start_business_with_new_dish(self):
        self.waiter.giveOrder('beef')
        self.waiter.giveOrder('pork')
        self.waiter.giveOrder('chicken')
        my_dish = self.waiter.sendOrder()
        return my_dish

def main():
    r = Restaurant()
    print(r.start_business_with_new_dish())

if __name__ == '__main__':
    main()
'''