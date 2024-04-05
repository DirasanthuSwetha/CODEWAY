def add(nums):
    return sum(nums)  # nums -> numbers


def subtract(nums):
    res= nums[0]   # res -> result
    for num in nums[1:]:
        res -= num
    return res


def multiply(nums):
    res = 1
    for num in nums:
        res *= num
    return res


def divide(nums):
    res = nums[0]
    for num in nums[1:]:
        if num == 0:
            return "Error! Division by zero."
        res /= num
    return res


def modulus(nums):
    res = nums[0]
    for num in nums[1:]:
        res %= num
    return res


def perform_operation(operation, numbers):
    return {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide,
        '5': modulus,
    }.get(operation, lambda nums: "Invalid operation.")(numbers)


print("Welcome to Simple Calculator")
while True:
    print("\n Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    operation = input("Enter choice (1/2/3/4/5/6): ")
    if operation == '6':
        print("Goodbye! Have a great day!")
        break

    num_type = input("Select number type (int/float): ")
    num_count = int(input("Enter how many numbers:".format(
        {

                '1': 'add',
                '2': 'subtract',
                '3': 'multiply',
                '4': 'divide',
                '5': 'perform modulus operation on',
        }[operation])))

    nums = []
    for i in range(num_count):
        nums.append(eval(num_type)(input("Enter number {}: ".format(i + 1))))

    result = perform_operation(operation, nums)
    print("Result:", result)
