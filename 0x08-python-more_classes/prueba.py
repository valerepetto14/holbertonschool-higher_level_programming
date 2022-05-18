class auto:
    autos = 0
    pais = "china"
    def __init__(self,marca,año):
        self.marca = marca
        self.año = año
        auto.autos += 1


my_auto = auto("nissan","1967")
my_auto.pais = "euu"
print(auto.pais)
print(my_auto.pais)
