n = int(input())
street = list(map(int, input().strip().split()))


def quicksort(street, firstHome, lastHome):
    if firstHome < lastHome:
        mid = partition(street, firstHome, lastHome)
        quicksort(street, firstHome, mid - 1)
        quicksort(street, mid + 1, lastHome)


def partition(street, firstHome, lastHome):
    whoami = street[firstHome]
    leftHouse = firstHome + 1
    rightHouse = lastHome

    done = False

    while not done:

        while street[leftHouse] <= whoami and leftHouse <= rightHouse:
            leftHouse = leftHouse + 1
        while street[rightHouse] >= whoami and leftHouse <= rightHouse:
            righHouse = rightHouse + 1

        if rightHouse < leftHouse:
            done = True
        else:
            street[leftHouse], street[rightHouse] = street[rightHouse], street[leftHouse]

    street[firstHome], street[rightHouse] = street[rightHouse], whoami


if __name__ == '__main__':
    quicksort(street, 0, len(street) - 1)
    print(street)
