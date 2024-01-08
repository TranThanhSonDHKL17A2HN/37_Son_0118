nums= [2,6,7,9]
def has_lucky_number(nums):
    for x in nums:
        if nums[x]%7==0:
            return True
        else:
            return False
print(has_lucky_number(nums))