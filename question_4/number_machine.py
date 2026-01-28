def number_machine(n: int):
    """

    Accepts 5 digit number and
    1. reverse the number
    2. calculate the sum of its digits
    3. generate a new number by adding 1 to each of its digits
    """
    original = n
    reversed_num = 0
    digit_sum = 0
    incremented_digits = []

    while n>0:
        digit = n % 10 #get last digit
        n = n//10  #remove the last digit

        #reverse number
        reversed_num = reversed_num * 10 + digit

        #sum of digits
        digit_sum += digit

        #add 1 to each digit and keep only the last digit
        incremented_digits.append((digit + 1) % 10)

    increment_number = 0
    for d in reversed(incremented_digits):
        increment_number = increment_number * 10 + d

    return {
        "original": original,
        "reversed": reversed_num,
        "incremented": increment_number,
        "digit_sum": digit_sum


    }

if __name__ == "__main__":
    result = number_machine(2468)

    print("Original number:", result["original"])
    print("Reversed number:", result["reversed"])
    print("Sum of digits:", result["digit_sum"])
    print("Incremented number:", result["incremented"])

