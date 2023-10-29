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
        current_lowest_index = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[current]:
                current_lowest_index = j
        lst[i], lst[current_lowest_index] = lst[current_lowest_index], lst[i]
        print(lst)
    return lst

def merge_sort(lst):

    if len(lst) > 1:

        mid = len(lst) // 2

        left = lst[:mid]
        right = lst[mid:]

        first = merge_sort(left)
        second = merge_sort(right)

        i = j = k = 0

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
                k += 1
            else:
                lst[k] = right[j]
                j += 1
                k += 1

        while len(left) > i:
            lst[k] = left[i]
            i+=1
            k+=1

        while len(right) > j:
            lst[k] = right[j]
            j+=1
            k+=1
        print(lst)

def main():
    lst = []
    for I in range(30):
        lst.append(random.randint(0,50))
    merge_sort(lst)    
    print(lst)

if __name__ == "__main__":
    main()