""" Calculate the first ten digits of the sum of each line in ./sourcefile."""
# Open file as list of its lines in string format
source = open('./sourcefile').readlines()
# Create empty list for lines in integer format
addends = []
# Fill list with lines in integer format
for i in source:
    addends.append(int(i))
# Print the first 10 digits of the sum of the list
print(str(sum(addends))[:10])

