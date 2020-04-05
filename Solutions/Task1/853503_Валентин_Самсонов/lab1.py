import argparse
import random


def wordCount(text):
    for symbols in ".,-\n":
        text = text.replace(symbols, ' ')

    text = text.lower()
    text = text.split()
    dic = {}
    list = []

    for word in text:
        if word not in dic:
            dic[word] = 0
        dic[word] = dic[word] + 1

    for key, value in dic.items():
        list.append([value, key])
    list.sort(reverse=True)

    print(list)
    print("top 10 words:")
    list = list[:10]
    for i in range(10):
        list[i] = list[i][1]
    s = ' '
    print(s.join(list))


def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2

        fsthalf = nums[:mid]
        lsthalf = nums[mid:]

        mergeSort(fsthalf)
        mergeSort(lsthalf)

        i, j, n = 0, 0, 0

        while i < len(fsthalf) and j < len(lsthalf):
            if fsthalf[i] < lsthalf[j]:
                nums[n] = fsthalf[i]
                i += 1
            else:
                nums[n] = lsthalf[j]
                j += 1
            n += 1

        while i < len(fsthalf):
            nums[n] = fsthalf[i]
            i += 1
            n += 1

        while j < len(lsthalf):
            nums[n] = lsthalf[j]
            j += 1
            n += 1


def quickSort(nums, fst, lst):
    if fst >= lst:
        return

    i, j = fst, lst
    p = random.choice(nums)

    while i <= j:
        while nums[i] < p:
            i += 1
        while nums[j] > p:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

    quickSort(nums, fst, j)
    quickSort(nums, i, lst)


def fibanachi(n):
    fib1 = 1
    fib2 = 1
    for i in range(n):
        fib2, fib1 = fib2 + fib1, fib2
        yield fib1


parser = argparse.ArgumentParser(description='Choice the program and file')

parser.add_argument("filename", type=str)
parser.add_argument('-w', "--wordcount", action="store_true")
parser.add_argument('-q', "--quicksort", action="store_true")
parser.add_argument('-m', "--mergesort", action="store_true")
parser.add_argument('-f', "--fibonacci", action="store_true")

args = parser.parse_args()
filename = args.filename

if args.wordcount:
    with open(filename, "r") as file:
        text = file.read()
    wordCount(text)

elif args.quicksort:
    with open(filename, "r") as file:
        numbers = file.read()

    numbers = numbers.split()
    numbers = list(map(int, numbers))
    fst = 0
    lst = len(numbers) - 1

    quickSort(numbers, fst, lst)

    for i in range(len(numbers)):
        print(numbers[i], end=" ")

elif args.mergesort:
    with open(filename, "r") as file:
        numbers = file.read()

    numbers = numbers.split()
    numbers = list(map(int, numbers))
    mergeSort(numbers)

    for i in range(len(numbers)):
        print(numbers[i], end=" ")

elif args.fibonacci:
    with open(filename, "r") as file:
        fib = int(file.read())

    for i in fibanachi(fib):
        print(i, end=' ')