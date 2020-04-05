import math


class Vector:
    def __init__(self, vec):
        self.vec = vec

    def printVector(self, v):
        return print(v.vec)

    def sumVector(self, v1, v2):
        list = []
        rez = Vector(list)
        i = 0
        while i < len(v1.vec):
            rez.vec.append(v1.vec[i] + v2.vec[i])
            i += 1
        return rez.printVector(rez)

    def subVector(self, v1, v2):
        list = []
        rez = Vector(list)
        i = 0
        while i < len(v1.vec):
            rez.vec.append(v1.vec[i] - v2.vec[i])
            i += 1
        return rez.printVector(rez)

    def multiVector(self, v, n):
        list = []
        rez = Vector(list)
        i = 0
        while i < len(v.vec):
            rez.vec.append(v.vec[i] * n)
            i += 1
        return rez.printVector(rez)

    def scalarVector(self, v1, v2):
        rez = 0
        i = 0
        while i < len(v1.vec):
            rez += v1.vec[i] * v2.vec[i]
            i += 1
        return rez

    def compareVector(self, v1, v2):
        if v1.vec == v2.vec:
            return print("Vectors are same")
        else:
            return print("Vectors are different")

    def lenVector(self, v):
        rez = 0
        i = 0
        while i < len(v.vec):
            rez += (v.vec[i] ** 2)
            i += 1
        length = math.sqrt(rez)
        return length


if __name__ == '__main__':

    vector = list()
    n = int(input("Input size = "))
    i = 0
    while i < n:
        v = int(input())
        vector.append(v)
        i += 1
    vector1 = Vector(vector)
    print("Next vector:")
    vector = list()
    i = 0
    while i < n:
        v = int(input())
        vector.append(v)
        i += 1
    vector2 = Vector(vector)

    print("Vector 1:")
    vector1.printVector(vector1)

    print("Vector 2:")
    vector2.printVector(vector2)

    print("Compare vectors:")
    vector1.compareVector(vector1, vector2)

    print("Sum of vectors:")
    vector1.sumVector(vector1, vector2)

    print("Sub of vectors:")
    vector1.subVector(vector1, vector2)

    n = int(input("Multiply of vector1 by constant = "))
    vector1.multiVector(vector1, n)

    print("Scalar multiply of vectors:")
    rez = vector1.scalarVector(vector1, vector2)
    print(rez)

    print("Length of vector 1:")
    rez = vector1.lenVector(vector1)
    print(rez)

testvec1 = Vector([1, 2, 3])
testvec2 = Vector([3, 2, 1])