def insert_squares(arr, num):
    i = 1
    while i < num + 1:
        arr.append(i * i)
        i = i + 1
    print(arr)
    # add square of numbers from 1 to num to the list named arr and return list