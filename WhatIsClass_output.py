import WhatIsClass
calorieBox= WhatIsClass.calorie_calculation()
calorieBox.carbo__Add(400)
calorieBox.fat____Add(100)
calorieBox_=calorieBox.calc()
print (calorieBox_)
####
shippingCalcBox= WhatIsClass.CalcFree()
shippingCalcBox.addItem(300)
shippingCalcBox.addItem(900)
print (shippingCalcBox.calc())
shippingCalcBox.shipping_fee=500
print (shippingCalcBox.calc())
