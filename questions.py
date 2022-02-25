# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

#     def hello_name(user_name):
#         .....

def hello_name(user_name):
    print("Hello" + user_name.upper() +"!")

hello_name('Lamont')

# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for num in range(1, 101, 2):
        print(num)
first_odds()

# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.


num_list = [25, 100, 600, 7, 15]
def max_list():
    print(max(num_list))


# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    return f'{year} is a leap year!' if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)  

is_leap_year(2016)


# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    if sorted(a_list) == list(range(min(a_list), max(a_list)+1)):
        return True
    else:
        return False
is_consecutive([7, 8,5,10])


