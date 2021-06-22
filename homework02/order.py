import restaurant as rst

class Restaurant:
    def __init__(self):
        self.waiter = rst.Waiter()
        self.cooker = rst.Cooker()
        self.waiter.cmd_dict['beef'] = rst.CommandOrderBeef(self.cooker)
        self.waiter.cmd_dict['chicken'] = rst.CommandOrderChicken(self.cooker)
        self.waiter.cmd_dict['pork'] = rst.CommandOrderPork(self.cooker)

 #globals()[customer_type.name.capitalize()+"Policy"]().count(prices)  

    def start_business_with_new_dish(self, order:list[str]):
        for l in order:
            self.waiter.giveOrder(l)
        my_dish = self.waiter.sendOrder()
        return my_dish

def main():
    r = Restaurant()
    order = ['beef', 'pork', 'chicken']
    r.start_business_with_new_dish(order)

if __name__ == '__main__':
    main()