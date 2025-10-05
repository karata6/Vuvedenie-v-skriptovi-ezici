numbers_input = input("Enter numbers with spaces in between: ")
numbers = [int(x) for x in numbers_input.split()]

special_numbers = []

for num in numbers:
    if num > 20 and num % 3 == 0 and num % 5 != 0:
        special_numbers.append(num)

print("special_numbers:", special_numbers)
