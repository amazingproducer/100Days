# A Pythagorean triplet is a set of three natural numbers, a < b < c, for
# which:  a^2 + b^2 = c^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# I think the brutish way to do this would be to make a list of the squares of
# each number up to 500 or something, then for each element, check if any other
# two elements can be summed to equal that element and add it to a second list.
# Then take each element from that second list and find the element for which
# the square roots of each subelement can be summed to equal 1000.

squares = []  # squares of all the numbers from 1 to 500 or something
triplets = []  # list of pythagorean triplets


def get_squares(a=1, b=500):
    for i in range(a, b):
        squares.append((i**2))


def get_triplets(a=1, b=500):
    get_squares(a, b)
    for i in squares:
        j = i  # Hold a value for the first addend
        for i in squares:
            if i > j:  # look for a second addend according to rules
                if (i + j) in squares:
                    triplets.append([int(j**.5), int(i**.5), int((j + i)**.5)])
    return triplets


def get_special(sum=1000):
    get_triplets(1, 500)
    for i in triplets:
        k = 0
        product = 1
        for j in i:
            k += j
            product *= j
        if k == 1000:
            return i, product


print(get_special())
