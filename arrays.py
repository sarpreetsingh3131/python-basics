""" Arrays """

# adding all elements of the array arr and returning the sum.


def sum(arr):
    total = 0
    for e in arr:
        total += e
    return total

# creating a string containing a nice-looking print out of the content of the array


def toString(arr):
    string = '{'
    for i in range(0, len(arr)):
        string += str(arr[i]) + ', '
    return string[:-2] + '}'

# creating and returning a new array, where n have been added to all elements in arr. Array arr should be left unchanged.


def addN(arr, n):
    array = arr
    for i in range(0, len(arr)):
        array[i] += n
    return array

# creating and returning a new array, consisting of all elements in arr in reverse order. Array arr should be left unchanged


def reverse(arr):
    array = []
    for i in range(len(arr) - 1, -1, -1):
        array.append(arr[i])
    return array

# returning true if n is contained in the array arr, false otherwise.


def hasN(arr, n):
    for e in arr:
        if e == n:
            return True
    return False

# replacing all occurrences of old with nw in arr.


def replaceAll(arr, old, nw):
    for e in arr:
        if e == old:
            e = nw

#  returning a new sorted array (increasing order), containing the same set of integers as arr. Array arr should be left unchanged.


def sort(arr):
    array = arr
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


arr = [1, 2, 3, 4, 5]

print(sum(arr))
print(toString(arr))
print(toString(addN(arr, 1)))
print(toString(reverse(arr)))
print(hasN(arr, 2))
print(toString(sort([2, 1, 4, 3, 2, 1])))
