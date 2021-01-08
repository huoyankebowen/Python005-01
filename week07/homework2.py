def map2(func,list1):
    list2=[]
    for i in list1:
        list2.append(func(i))
    return list2


def f(num):
    return num+1

print(map2(f,[1,2,3,4,5,6,7]))