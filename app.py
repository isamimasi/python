#############################
#
#python 3.11.3
#2024-05-10 v1.0
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
"""
fee1 = CalcFree()
fee1.addItem(500)
fee1.addItem(100)
print (fee1.calc())
###
fee2= CalcFree()
fee2.shipping_fee = 1500
fee2.addItem(800)
print (fee2.calc())
"""
