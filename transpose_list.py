# homework:
#   [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
#   [ [1, 4, 7], [2, 5, 8], [3, 6, 9] ]

list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
# data = [[], [], []]
data = []
for i in range(len(list_of_lists)):
    data.append([])
    for _lists in list_of_lists:
        # print(data)
        data[i].append(_lists[i])# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        # data.append(_lists[i])#[ 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(data)
