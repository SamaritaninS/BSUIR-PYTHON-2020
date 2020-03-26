import math


class Vector:
    def __init__(self, x, size):
        self.x = x
        self.size = size

    def createVector(self):
        for i in range(self.size):
            i = int(input())
            self.x.append(i)

    def getVector(self):
        vector = list()
        for i in self.x:
            vector.append(i)
        return vector


    def sumVector(self, v1):
        v2 = list()
        a = 0
        while a < self.size:
            i = self.x[a] + v1.x[a]
            v2.append(i)
            v1.x[a] = i
            a += 1
        return v1

    def subVector(self, v1):
        v2 = list()
        a = 0
        while a < self.size:
            i = self.x[a] - v1.x[a]
            v2.append(i)
            v1.x[a] = i
            a += 1
        return v1

    def multiVector(self, a):
        vector = list()
        i = 0
        while i < self.size:
            v = (self.x[i] * a)
            vector.append(v)
            self.x[i] = v
            i += 1
        return vector

    def scalarVector(self, v1):
        result = 0
        i = 0
        while i < self.size:
            result += self.x[i] * v1.x[i]
            i += 1
        return result

    def compareVector(self, v1):
        if self.x == v1.x:
            return True
        else:
            return False

    def lenVector(self):
        i = 0
        result = 0
        while i < self.size:
            result += (self.x[i] ** 2)
            i += 1
        length = math.sqrt(result)
        return length


if __name__ == '__main__':

    vector = list()
    n = int(input())
    a = 0
    while a < n:
        v = int(input())
        vector.append(v)
        a += 1

    vector1 = Vector(vector, n)
    vector2 = Vector([0, 1, 1], 3)
    print("Vector 1:")
    print(vector1.getVector())
    print("Vector 2:")
    print(vector2.getVector())
    print("Sum of vectors:")
    print(vector1.sumVector(vector2).getVector())
    print("Sub of vectors:")
    print(vector1.subVector(vector2).getVector())
    print("Compare of vectors:")
    print(vector1.compareVector(vector2))
    print("Multiple of vectors:")
    print(vector1.multiVector(3))
    print("Scalar product of vectors:")
    print(vector1.scalarVector(vector2))
    print("Length of vector:")
    print(vector1.lenVector())
