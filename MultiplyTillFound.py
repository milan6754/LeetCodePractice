def multiply_till_found(num, list):
    for num in list:
        num*=2
    return num

print(multiply_till_found(2,[1,2,3,4,5,6,7,8]))