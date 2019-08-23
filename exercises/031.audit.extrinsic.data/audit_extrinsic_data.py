import json

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
        for char in n[field]:
            print(char, typename)
            if type(char).__name__ != typename:
                return False
        return True




