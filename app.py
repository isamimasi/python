#############################
#
#
#############################
import math
class CalcFree:
    def __init__(self):
        '''初期化'''
        self.shipping_fee = 1000
        self.tax_rate = 0.08
        self.value = 0
    def addItem(self, price):
        self.value += price
    def calc(self):
        '''sum final '''
        total = self.value + self.shipping_fee
        tax = math.ceil(total * self.tax_rate)
        v= math.ceil (total + tax)
        return v