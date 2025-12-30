def sub_until_zero(num1,num2):
    operation = 0 
    while num1!=0 and num2!=0:
        if num1>=num2:
            num1-=num2
        else:
            num2-=num1
        operation+=1
    return operation

print(sub_until_zero(5,2))
