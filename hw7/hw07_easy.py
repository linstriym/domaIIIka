# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
#TODO:
import math
 
 
class Triangle:
    def __init__(self, A, B, C):
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)
        self.A = A
        self.B = B
        self.C = C
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CA = sideLen(self.C, self.A)
    # Вычисление по формуле Герона
    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2
        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.AB)
                         * (semi_perimeter - self.BC)
                         * (semi_perimeter - self.CA))
    def perimeterTriangle(self):
        return self.AB + self.BC + self.CA
    # высота
    def heightTriangle(self):
        return self.areaTriangle() / (self.AB / 2)
treugolnik1 = Triangle((6, 4), (13, 18), (5, 27))
print(treugolnik1.areaTriangle())
print(treugolnik1.heightTriangle())
print(treugolnik1.perimeterTriangle())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
#TODO:
import math
class Trapeze():

    def __init__(self, coord_a, coord_b, coord_c, coord_d):
        self.coord_a = coord_a
        self.coord_b = coord_b
        self.coord_c = coord_c
        self.coord_d = coord_d
        self.side_a = math.sqrt((coord_b[0] - coord_a[0]) ** 2 + (coord_b[1] - coord_a[1]) ** 2)
        self.side_b = math.sqrt((coord_c[0] - coord_b[0]) ** 2 + (coord_c[1] - coord_b[1]) ** 2)
        self.side_c = math.sqrt((coord_d[0] - coord_c[0]) ** 2 + (coord_d[1] - coord_c[1]) ** 2)
        self.side_d = math.sqrt((coord_a[0] - coord_d[0]) ** 2 + (coord_a[1] - coord_d[1]) ** 2)
    @property
    def perimeter(self):
        return (self.side_a + self.side_b + self.side_c + self.side_d)
    @property
    def square(self):
        return (self.side_b + self.side_d / 4 * math.sqrt(4 * self.side_b - (self.side_b - self.side_d) ** 2))
    @property
    def isosceles(self):
        return True if self.side_a == self.side_c else False
coord_trap_a = (-2, 2)
coord_trap_b = (-4, -2)
coord_trap_c = (4, -2)
coord_trap_d = (2, 2)
trap = Trapeze(coord_trap_a, coord_trap_b, coord_trap_c, coord_trap_d)
print(trap.isosceles)
print(trap.square)
print(trap.perimeter)

