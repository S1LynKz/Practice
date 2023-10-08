# written by Jayden Sun
# Implementation of different sorting algorithms
import random

def iteration_sort(lst):
    for i in range(1, len(lst)):
        current = i
        while (lst[current] < lst[current - 1] and current > 0):
            print(lst)
            lst[current], lst[current - 1] = lst[current - 1], lst[current]
            current = current - 1
    return lst

def selection_sort(lst):
    for i in range(len(lst)):
        current = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[current]:
                current = j
        lst[i], lst[current] = lst[current], lst[i]
        print(lst)
    return lst

def main():
    lst = []
    for I in range(30):
        lst.append(random.randint(0,50))
    print(lst)
    print(selection_sort(lst))

if __name__ == "__main__":
    main()