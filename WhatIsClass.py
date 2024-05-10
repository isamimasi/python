class calorie_calculation:
    def __init__(self):
        '''初期化'''
        self.fat = 0
        self.carbo = 0
        self.protein = 0
        self.totalCalorie = 0
    def carbo__Add(self,carbo):
        self.totalCalorie+=carbo*4
    def proteinAdd(self,prot):
        self.totalCalorie+=prot*4
    def fat____Add(self,fat_):
        self.totalCalorie+=fat_*9
    def calc(self):
        return self.totalCalorie
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

