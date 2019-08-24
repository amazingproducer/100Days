import json
import re

user_inputs_file = open('./user_input_data.json')
user_input = json.load(user_inputs_file)

reserved_usernames_file = open('./reserved-usernames.json')
reserved_usernames = json.load(reserved_usernames_file)

# I just realized I have no idea what I should make this do
# I have a big ol' list of audits to make, which should be made against
# each element of the dataset. I guess I make a thing that eats user entries.

class UserAudit():
    def required_field(n, field):
        if not n[field]:
            return False
        return True


    def invalid_substring(n, field, invalid_list):
        for i in invalid_list:
            if n[field]:
                if i in n[field]:
                    return False
        return True


    def required_length(n, field, min, max):
        if n[field]:
            if min <= len(n[field]) and len(n[field]) <= max:
                return True
        return False


    def required_type(n, field, typename):
        if not n[field]:
            return False
        if typename == "alnum":
            if not n[field].isalnum():
        if typename == "digit":
            if not n[field].isdigit():
                return False
        elif typename == "alpha":
            if not n[field].isalpha():
                return False
        return True


    def regex_match(n, field, reg):
        if not n[field]:
            return False
        if re.match(reg, n[field]) == n[field]:
            return True
        return False


