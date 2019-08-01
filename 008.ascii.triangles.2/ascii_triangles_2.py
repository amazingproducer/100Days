# You must create a program that echoes a Triforce of a given size n.
# A triforce is made of 3 identical triangles
# A triangle of size n should be made of n lines
# A triangle's line starts from 1 star, and earns 2 stars each line

# For example, a Triforce of size 3 will look like:

#      *
#     ***
#    *****
#   *     *
#  ***   ***
# ***** *****



class triforce:
    def left_pad(line, height):
        return (2 * height) - line

    def center_pad(line, height):
        if line > height:
            return (4 * height) - ((line * 2) -1)
        return 0

    def point_count(line, height):
        return ((2 * line) - 1) - triforce.center_pad(line, height)

    def abstract(height):
        line_count = 1
        while line_count <= height:
            print(line_count, triforce.left_pad(line_count, height), triforce.point_count(line_count, height))
            line_count += 1
        while line_count <= (2 * height) and line_count > height:
            print(line_count, triforce.left_pad(line_count, height), triforce.point_count(line_count, height), triforce.center_pad(line_count, height))
            line_count += 1

triforce.abstract(3)
