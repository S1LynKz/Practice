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
# lst = ["jayden", "kevin", "anna", "bob", "lee", "yvonne", "ivan", "1", "2", "3", "76", "8", "5", "33"]

def main():
    lst = []
    for I in range(30):
        lst.append(random.randint(0,100))
    print(iteration_sort(lst))

if __name__ == "__main__":
    main()