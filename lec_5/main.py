def sum_of_elements(numbers, exclude_negative=False):
    if exclude_negative:
        numbers = [number for number in numbers if number >= 0]
    return sum(numbers)


input_numbers = input("Enter a list of numbers separated by spaces: ")
user_numbers = [int(number) for number in input_numbers.split()]

exclude_negative_input = input("Do you want to exclude negative numbers? (yes or no): ").strip().lower()
exclude_negative = exclude_negative_input == "yes"

total_sum = sum_of_elements(user_numbers, exclude_negative)

if exclude_negative:
    print("Sum of non-negative numbers:", total_sum)
else:
    print("Sum of all numbers:", total_sum)
