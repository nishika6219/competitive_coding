#given an array return an array where each element is the product of all the elements in the array except itself
#logic  use two passes one from left to right and one from r to l to calculate product
# input [1,2,3,4] output [ 24,12,8,6]

def product(nums):
    n = len(nums)
    result = []

    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        result.append(prod)

    return result


print(product([1, 2, 3, 4]))  # [24, 12, 8, 6]