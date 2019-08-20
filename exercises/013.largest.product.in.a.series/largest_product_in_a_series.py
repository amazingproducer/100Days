
big_series = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

# The four adjacent digits in that giant number up there that have the greatest
# product 9 x 9 x 8 X 9, the product of which is 5832.
# Find the thirteen adjacent digits in that giant number up there that have the
# greatest product. What is the value of that product?

# hrm. I think a naive way to do this is to scan the giant number up there
# for 13 nines in a row, then 12 nines and an 8 or something? I guess I could
# also build a list of the 1000-13 products and see which is highest with some
# list comprehension thingies. Let's try that :3

# Ok so I want a thingy that accepts a range, the bounds of which are declared
# as arguments, as well as a numerical sequence, and returns the product of the
# numbers of the sequence within the given range. Let's make a clumsy attempt
# at that.

def get_product_from_segment(a, b, x=big_series):
    a -= 1
    b += 1
    c = 1
    for i in range(a, b):
        c *= int(x[i])
#    return c, x[a:b] # superfluous
    return c

# Okay, so this thing works. Now what do we do with it? I think I want to take
# a lower limit, upper limit, and a numerical string, then call the
# get_product_from_segment() function, adding its result to a list. then
# increment the upper and lower limit by one and call the function again until
# the upper limit equals the length of the original string. Finally, return the
# highest value in the list and its corresponding substring.

# On second thought, let's build a dictionary for this data instead.

def solve(lower_limit=1, upper_limit=4, x=big_series):
    a = lower_limit
    b = upper_limit -1
    p = [] # a list of our products
    q = [] # a list of their corresponding factors
    while b < len(x):
#    while b < (len(x) - 900): # debug loop
        p.append(get_product_from_segment(a, b, x))
        q.append(x[(a - 1):(b + 1)])
#        print(x[(a-1):(b+1)]) # debug print
        a += 1
        b += 1
    z = p.index(max(p))
#    print(q)
#    print(z)
    return max(p), q[z]
e = solve()
print(f"Example data - Highest Product: {e[0]}, Sequence: {e[1]}")
q = solve(1, 13)
print(f"Exercise data - Highest Product: {q[0]}, Sequence: {q[1]}")

