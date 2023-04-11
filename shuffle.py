import random

def shuffle(lst):
    new_lst = []
    for i in range(len(lst)):
        rand_index = random.randint(0, len(lst)-1)
        # print(rand_index)
        new_lst.append(lst[rand_index])
        lst.pop(rand_index)
    return new_lst

print(shuffle([1,2,3,4,5]))