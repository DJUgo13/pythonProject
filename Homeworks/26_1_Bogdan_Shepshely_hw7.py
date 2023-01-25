numbers = [9, 8, 5, 3, 7, 2, 1, 4, 6]


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


if __name__ == '__main__':
    lst = numbers
    bubble_sort(lst)
    print("Sorted list is: ", lst)


data = []


def binary_search(list, number):
    l = list[0]
    r = list[-1]
    m = len(list) // 2
    while True:
        if m < number:
            data.append(m)
            l = m
            m = (l + r) // 2
        elif m > number:
            data.append(m)
            r = m
            m = (l + m) // 2
        elif m == number:
            data.append(m)
            return "всё!"


print(binary_search(range(1, 51), 12), f"{data} количество попыток - {len(data)}")

sort_lst = []



