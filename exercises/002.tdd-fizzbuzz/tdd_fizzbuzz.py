class FizzBuzz:
    def replace_numbers(upper_limit=1, lower_limit=101):
        fb_list = []
        for i in range(upper_limit, lower_limit):
            if i % 15 == 0:
                fb_list.append("FizzBuzz")
            elif i % 5 == 0:
                fb_list.append("Buzz")
            elif i % 3 == 0:
                fb_list.append("Fizz")
            else:
                fb_list.append(str(i))
        print(*fb_list, sep='\n')
        return fb_list


