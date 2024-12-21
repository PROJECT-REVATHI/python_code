def filteing(nums):

    def is_odd(nums):
        return nums % 2 == 0
    

    filter_even = list(filter(is_odd,nums))
    return filter_even







nums = [1,2,3,4,5,6,7,8,10]
res = filteing(nums)
print(res)