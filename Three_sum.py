def two_sum(list,target):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            for k in range (j+1,len(list)):
                if list[i] +list[j] + list[k]== target:
                    return (list[i],list[j],list[k])

list=[1,2,3,4,5,6,7,8,9]
target=13
print(two_sum(list,target))