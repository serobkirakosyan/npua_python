def classify_numbers(numbers):
    even_numbers = []

    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers, odd_numbers


numbers = input("Enter a list of numbers separated by spaces: ")
user_numbers = [int(num) for num in numbers.split()]

even_numbers, odd_numbers = classify_numbers(user_numbers)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
