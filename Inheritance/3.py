class vehical:
    def wheels(self,w=" "):
        print(w)
    def speed(self,s):
        print(s)
    def brand(self,b):
        print(b)

class car(vehical):
    def input_item(self):
        wheel_ = input("enter the wheel name   : ")
        super().wheels(wheel_)
        speed_ = int(input("enter the speed : _"))
        super().speed(speed_)
        brand_ = input("enter the brfand : ")
        super().brand(brand_)

o = car()
o.input_item()
