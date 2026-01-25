def not_divisiable_by_three(nums):
    operation = 0 

    for num in nums:
        if num %3 !=0:
            operation +=1

    return operation

print(not_divisiable_by_three([1,2,3,4,6,5]))