# write a python code to find if the given number is odd or even?


#solution

def check_odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))
result = check_odd_or_even(num)
print(f"The number {num} is {result}.")
