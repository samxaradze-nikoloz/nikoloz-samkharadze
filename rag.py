class Circle:
    pi=3.14
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return Circle.pi * (self.radius ** 2)
circle=Circle(5)
area=circle.calculate_area()
print(f"radiusi da fartobi aris{circle.radius} is {area}")

class house:
    def __init__(self, size, color):
        self.size=size
        self.color=color
    def housee(self):
      return f"house size is {self.size} and hoise is painted {self.color}"       
housea=house("100sqm","blue")
houseb=house("200sqm", "red")
print(housea.housee())
print(houseb.housee())