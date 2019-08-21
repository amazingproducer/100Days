# Draw a triangle that looks liek this:
#
# #
# ##
# ###
# ####
# #####
# ######


def draw_triangle(limit: int = 6):
    i = 0
    j = ""
    while i < limit:
        j += "#"
        print(j)
        i += 1


draw_triangle()
