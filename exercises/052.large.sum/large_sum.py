# Calculate the first ten digits of the sum of each line in ./sourcefile

# I Think the quickest way to solve this is to incrementally take a slice of
# one decimal place for each line in sourcefile and amassing the sum of each
# slice until reaching 10^9, but I think the first ten digits are not the ones
# that start with 10^0 place.

# Perhaps I simply have to get a sum of each number and slice from the 11th
# digit.


# Open file as list of its lines in string format
source = open('./sourcefile').readlines()
# Create empty list for lines in integer format
addends = []
# Fill list with lines in integer format
for i in source:
    addends.append(int(i))
# Print the first 10 digits of the sum of the list
print(str(sum(addends))[:10])

