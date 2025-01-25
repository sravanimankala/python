#abstraction
from abc import ABC
class polygon(ABC):
    def sides(self):
        pass
class triangle(polygon):
    def sides(self):
        print("triangle has 3 sides")
class square(polygon):
    def sides(self):
        print("square has 4 sides")
class pentagon(polygon):
    def sides(self):
        print("pentagon has 5 sides")            
t=triangle()
t.sides()
s=square()
s.sides()
p=pentagon()
p.sides()   