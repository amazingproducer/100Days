#  Given n non-negative integers representing an elevation map where the width
#  of each bar is 1, compute how much water it is able to trap after raining.

# Do what now?
# I never considered the rules of what makes a water trap:

# To capture water at a given point, the elevation of one of its neighboring
# points must be greater than that of its own. - not true

# The number of units a given point contributes to water capture does not
# appear to be calculable solely by the elevation of its immediate neighbors.

# The minimum number of units a given point contributes to water capture, given
# that it can capture water, is equivalent to its difference in elevation with
# the lower of its neighbors. - not true

# Let's take a look at the example set and its result:
# The array [0,1,0,2,1,0,1,3,2,1,2,1] will trap 6 units of water.

# array[0] is 0 and if we can trust that a space must at least be greater than
# zero to be tall enough to contribute to water capture, then it cannot
# contribute to water capture. We could also reason that no further elements
# will capture water until a nonzero elevation appar.

# array[1] is 1 and can contribute to the capture of 1n units of water, where n
# is element width(1).

# array[2] is 0 and could capture no more than 1 unit of water.

# array[3] is 2 and can contribute to the capture of up to 2n units of water,
# where n is element width(1)

# array[4] is 1 and reduces the potential contribution of array[3] by 1n. It
# can contribute to the capture of up to 1n - wait wth am I doing?

# let's start from the top. of the elevation map. we know that the highest
# values become the brims of our vessels, so let's find those bounds.

# let's examine the array again: [0,1,0,2,1,0,1,3,2,1,2,1]
# our highest point is array[7] (3), and it is unique in the set, so while it
# is the highest number in the set, it will not be the high water mark. It
# will, however, contribute to the capture of water at the high water mark.

# the next highest value is 2, the first of which, array[3] has intersections
# with our highest point, array[7]. We can count on 3 units of capture at
# elevation 2 from array[4] to array[6].

# the next element at elevation 2 is array[8], which, captures no water but
# serves as the high water mark with its intersecting point, array[10]. We can
# count on 1 unit of capture at elevation 2 from array[9].

# now let's look along the high water ranges we just established and check
# their depth at each point. Anything deeper than 1 is previously unaccounted
# water

# array[4] is 1 so its depth is 1.
# array[5] is 0 so its depth is 2. we can count on 1 additional capture unit
# array[6] is 1 so its depth is 1.
# array[9] is 1 so its depth is 1.

# the next highest value is 1. the only element not accounted or eliminated is
# array[1], which intersecs at array[3],  We can count on one more capture unit
# from array[2].

# This brings our total to 3+1+1+1=6

# I think I understand why this exercise is categorized as 'hard'
