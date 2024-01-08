from enum import Enum
from typing import List


#######################
# Task1
#######################
class Counter:
  def __init__(self):
    pass

  def count(self, prices:List[int]):
    '''Calculate the final price based on given list of price.

    The calculation should follow the below policy:
    If the total price is less than 100, keep the original price: input=99, output=99
    If the total price is between [100~200], take 10% off: input=200, output=180
    If the total price is between [201~500], take 20% off: input=500, output=400
    If the total price is greater than 500, take 40% off. If the calculated price is less than 400, use 400:
      - input=600, output=max(400, 600*0.6)=max(400, 360)=400
      - input=1000, output=600

    If float number is obtained after calculation, use floor to translate it into integer.
    '''
    # TBD
    pass



#######################
# Task2
#######################
class CustomerType(Enum):
        NORMAL=0
        MEMBER=1
        VIP=3


class CounterV2:
  def __init__(self):
    pass

  def count(self, prices:List[int], customer_type:CustomerType):
    '''Calculate the final price based on given list of price according to customer type

    - If the customer is VIP: Use same discount policy as Counter
    - If the customer is a member: Always take 10% off.
    - Otherwise, no discount at all.
    '''
    # TBD
    pass
