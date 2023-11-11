from random import randint

numbers = []
for i in range(20):
    numbers.append(randint(0, 100))


def sot_list_imperative(nums):
    sw = True
    while sw:
        sw = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                sw = True
    print(f'imperative: {nums}')


def sot_list_declarative(lst):
    print(f'declarative: {sorted(lst, reverse=True)}')


sot_list_imperative(numbers)
sot_list_declarative(numbers)
