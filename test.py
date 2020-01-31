from enum import Enum

class A(Enum):
        HORSE = 1
        COW = 2
        CHICKEN = 3
        DOG = 4

x = A.COW
print(x)
print(A.COW == x)