# Write a program in a class named StarFigure that produces the following output
# using for loops:
#
# ////////////////\\\\\\\\\\\\\\\\
# ////////////********\\\\\\\\\\\\
# ////////****************\\\\\\\\
# ////************************\\\\
# ********************************

# What's going on here? Let's see....

# The first line takes one kind of slash for half of its length and another for
# the other half.

# The second line is a copy of the previous line, but replaces the central eight
# slashes with asterisks.

# The third line is a copy of the previous line, but replaces the four slashes
# nearest to the asterisk body on either side with additional asterisks.

# The fourth line can be characterized in the same manner as the previous line.

# The fifth line can be characterized in the same manner as the previous line.

# Width equals (linecount -1) * 8
# First line is always slashes
# Final line is always asterisks

class StarFigure:
