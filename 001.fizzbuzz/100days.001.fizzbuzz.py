#100days.001.fizzbuzz.py
# Objective: "Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the
# multiples of five print “Buzz”. For numbers which are multiples of both
# three and five print “FizzBuzz”."
# Revision 1: Allow user input of upper limit
# Revision 2: Refactor variables as sets
# Revision 3: Allow user input of upper and lower limits, support negative
#    integers
# Revision 4: Actually use the prescribed strings ("Fizz" vs "fizz")
# Revision 5: eliminiate mod15 check

user_lower_limit = input("Fizzbuzz - Enter lower limit: ")
try:
    lower_limit = int(user_lower_limit)
except:
    print("Error: input must be integer")
    raise
user_upper_limit = input("Enter upper limit: ")

try:
    upper_limit = int(user_upper_limit) + 1
except:
    print("Error: input must be integer")
    raise

if lower_limit >= upper_limit:
    print("Error: lower limit must be lesser than upper limit.")
    exit()

for i in range(lower_limit, upper_limit):
    j = ""
    if i % 3 == 0:
        j = "Fizz"
    if i % 5 == 0:
        j += "Buzz"
    else:
        j = i
    print(j)

