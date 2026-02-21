import random
import time

def selection_sort(list):
    comp = 0

    if len(list) == 0 or len(list) == 1:
        return comp

    if len(list) == 2:
        if list[0] == list[1]:
            comp += 1
            return comp
        elif list[0] > list[1]:
            comp += 1
            temp = list[0]
            list[0] = list[1]
            list[1] = temp
            return comp

    for i in range(len(list) - 1):
        min_spot = i
        for j in range(i + 1, len(list)):
            comp += 1
            if list[j] < list[min_spot]:
                min_spot = j
        temp = list[i]
        list[i] = list[min_spot]
        list[min_spot] = temp
    return comp

def insertion_sort(list):
    comp = 0

    if len(list) == 0 or len(list) == 1:
        return comp

    if len(list) == 2:
        if list[0] == list[1]:
            comp += 1
            return comp
        elif list[0] > list[1]:
            comp += 1
            temp = list[0]
            list[0] = list[1]
            list[1] = temp
            return comp

    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
            comp += 1
        list[j + 1] = key
        comp += 1
    return comp

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 1000)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

