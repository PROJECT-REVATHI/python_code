def filtering(nums, threshold):

    def is_threshold(nums):
        return nums <= threshold
    
    filtered_nums = list(filter(is_threshold,nums))

    return filtered_nums




nums = [20,30,40,50,60,50,7,4,3,2]
threshold = 8
content = filtering(nums, threshold)
print(content)


