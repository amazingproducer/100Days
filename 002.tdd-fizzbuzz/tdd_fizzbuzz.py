class FizzBuzz:
    def replace_numbers(upper_limit=1, lower_limit=101):
        fb_list = []
        for i in range(upper_limit, lower_limit):
            if i % 15 == 0:
                fb_list.append("FizzBuzz")
            elif i % 5 == 0:
                fb_list.append("Buzz")
            else:
                fb_list.append(str(i))
        return fb_list

