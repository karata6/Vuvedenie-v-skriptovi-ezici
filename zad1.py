def sum_list(nums):
    total = 0
    #obhojdane na spisuka s chisla i vsqko chislo se pribravq kum sumata na chislata ot spisuka predi nego
    for x in nums:
        total += x
    return total

def sum_list_rec(nums):
    #proverqva dali nums e prazen, false
    if not nums:
        return 0
    return nums[0] + sum_list_rec(nums[1:])

nums = [5, 3, 10, 7, 2]
print(sum_list(nums))
print(sum_list_rec(nums))