List_x = list(range(0,10))
print(List_x)
List_y = list(range(0, 10, 2))
print(List_y)
Empty_list = []
print(Empty_list)

def intersection(List_x, List_y):


    Empty_list = []
    for i in List_x:
        if i in List_y:
            Empty_list.append(i)
    return Empty_list



print("Новый список =", intersection(List_x, List_y))
