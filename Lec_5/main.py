def sum_of_elements(numbers, exclude_negative=False):
    if exclude_negative:
        numbers = [num for num in numbers if num >= 0]
    return sum(numbers)


user_input = input("Enter a list of numbers separated by spaces: ")
try:
    numbers = list(map(float, user_input.split()))
except ValueError:
    print("Invalid input! Please enter valid numbers separated by spaces.")
    exit(1)

while True:
    exclude_neg_input = (
        input("Do you want to exclude negative numbers? (yes or no): ").strip().lower()
    )
    if exclude_neg_input in ("yes", "no"):
        break
    else:
        print("Invalid input! Please enter 'yes' or 'no'.")

exclude_negative = exclude_neg_input == "no"


if exclude_negative:
    filtered_numbers = [num for num in numbers if num >= 0]

    print(
        "Filtered numbers (negative numbers excluded):",
        [int(num) if num.is_integer() else num for num in filtered_numbers],
    )
else:

    print(
        "All numbers included:",
        [int(num) if num.is_integer() else num for num in numbers],
    )

result = sum_of_elements(numbers, exclude_negative=exclude_negative)

if result.is_integer():
    result = int(result)

print(f"The sum of the elements is: {result}")
