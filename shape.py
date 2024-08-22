li = [2,9,5,4,8,1]




def bubble_sort(nums:list):

    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            first = nums[j]
            if nums[j] > nums[j + 1]:
                nums[j] = nums[j + 1]
                nums[j + 1] = first
        print(nums)
    return nums



print(bubble_sort(li))