class india:
    def capital(self):
        print("the capital of india is new Delhi")
    def lang(self):
        print("the primary language of india is Hindi")
    def type(self):
        print("inida is a developing country")

class usa:
    def capital(self):
        print("the capital of usa is washington D.C")
    def lang(self):
        print("the primary language of USA is English")
    def type(self):
        print("USA is a developed country")

obj1= india()
obj2= usa()
for country in(obj1, obj2):
    country.lang()
    country.type()
    country.capital()