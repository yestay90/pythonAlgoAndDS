
def finderMy(arr1, arr2):

    count = {}

    for num in arr1:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in arr2:
        if num in count:
            count[num] -= 1
        else:
            count[num] = 1

    for k in count:
        if count[k] != 0:
            print(k)
            print("is missing")

def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]

import collections

def finder2(arr1,arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

