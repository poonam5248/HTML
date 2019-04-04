print("Input 1:LINEAR SEARCH \n"
      "Input 2:BINARY SEARCH \n"
      "Input 3:INSERTION SORT \n"
      "Input 4:SELECTION SORT \n"
      "Input 5:BUBBLE SORT \n")

n = int(input("Enter from above choices:"))

if n == 1:
    print("Linear Search")
    lst = []
    num = int(input("Enter size of list: \t"))
    for n in range(num):
        numbers = int(input("Enter any number: \t"))
        lst.append(numbers)

    x = int(input("\nEnter number to search: \t"))

    found = False

    for i in range(len(lst)):
        if lst[i] == x:
            found = True
            print("\n%d found at position %d" % (x, i+1))
            break
    if not found:
        print("\n%d is not in list" % x)


elif n==2:
    print("Binary Search")


    def binary_sort(sortedlist, n, x):
        start = 0
        end = n - 1

        while (start <= end):
            mid = (start + end) / 2
            if (x == sortedlist[mid]):
                return mid
            elif (x < sortedlist[mid]):
                end = mid - 1
            else:
                start = mid + 1

        return -1


    n = input("Enter the size of the list: ")

    sortedlist = []

    for i in range(n):
        sortedlist.append(input("Enter %dth element: " % i))

    x = input("Enter the number to search: ")
    position = binary_sort(sortedlist, n, x)

    if (position != -1):
        print("Entered number %d is present at position: %d" % (x, position+1))
    else:
        print("Entered number %d is not present in the list" % x)

elif n == 3:
    print("Insertion Sort")
    a = []
    num = int(input("Enter size of list: \t"))
    for n in range(num):
        numbers = int(input("Enter any number: \t"))
        a.append(numbers)

    # iterating over a
    for i in a:
        j = a.index(i)
        # i is not the first element
        while j > 0:
            # not in order
            if a[j - 1] > a[j]:
                # swap
                a[j - 1], a[j] = a[j], a[j - 1]
            else:
                # in order
                break
            j = j - 1
    print (a)

elif  n==4:
    print("Selection Sort")
    a = []
    num = int(input("Enter size of list: \t"))
    for n in range(num):
        numbers = int(input("Enter any number: \t"))
        a.append(numbers)

    i = 0
    while i < len(a):
        # smallest element in the sublist
        smallest = min(a[i:])
        # index of smallest element
        index_of_smallest = a.index(smallest)
        # swapping
        a[i], a[index_of_smallest] = a[index_of_smallest], a[i]
        i = i + 1
    print (a)

elif  n==5:
    print("Bubble Sort")
    a = []
    num = int(input("Enter size of list: \t"))
    for n in range(num):
        numbers = int(input("Enter any number: \t"))
        a.append(numbers)

    # repeating loop len(a)(number of elements) number of times
    for j in range(len(a)):
        # initially swapped is false
        swapped = False
        i = 0

        while i < len(a) - 1:
            # comparing the adjacent elements
            if a[i] > a[i + 1]:
                # swapping
                a[i], a[i + 1] = a[i + 1], a[i]
                # Changing the value of swapped
                swapped = True
            i = i + 1
        # if swapped is false then the list is sorted
        # we can stop the loop
        if swapped == False:
            break
    print (a)

else:
    print(" Wrong Input")
