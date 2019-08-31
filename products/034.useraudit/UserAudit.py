#!/usr/bin/python3

# Usage: UserAudit.py [FILE] [OPTIONS]

# Audits the provided user dataset FILE and reports its validity.

# Optionally, when the program is executed with the -m or --merge arguments (and
# the required file argument), audits are conducted on both files before an
# attempt is made to merge the provided user input data with the existing
# dataset. The net result of each file's audits and the merget attempt are then
# reported to the user.

# The user may declare the following optional arguments:
# --reserved [filename] | use provided username blacklist (JSON)
# --titles [filename]   | use provided job title whitelist (JSON)
# --merge [filename]    | attempt to merge provided JSON file with dataset
# --purge               | remove invalid entries as they are encountered
# -v                    | increase output verbosity

# This program includes a set of configuration files, which are used by default:
# reserved_usernames.json: JSON array representing example blacklist
# valid_user_titles.json: JSON array representing example whitelist


from DataAudit import DataAudit as da
import argparse
from inspect import ismethod

def load_users_dataset(file):
    global ua_dataset
    ua_dataset = da.open_dataset(file)

def load_reserved_usernames(file='./reserved_usernames.json'):
    global ua_username_blacklist
    ua_username_blacklist = da.open_list(file)

def load_valid_job_titles(file='./valid_user_titles.json'):
    global ua_title_whitelist
    ua_title_whitelist = da.open_list(file)


class UserAudits():
    def name_and_email_fields_required(self):
        failset = []
        for i in ua_dataset[0]:
            if None in [i['first_name'], i['last_name'], i['auth_email']]:
                failset.append(i)
        if len(failset):
            return "FAIL"
        return "PASS"

    def username_must_not_contain_reserved_words(self):
        failset = []
        for i in ua_dataset[0]:
            for j in ua_username_blacklist:
                if i['username'] in j:
                    failset.append(i)
        if len(failset):
            return "FAIL"
        return "PASS"

    def email_and_usernames_must_be_unique(self):
        # This method isn't aware of what should be purged
        usernames = [i['username'] for i in ua_dataset[0]]
        email_addresses = [i['auth_email'] for i in ua_dataset[0]]
        if len(usernames) != len(set(usernames)):
            return "FAIL"
        if len(email_addresses) != len(set(email_addresses)):
            return "FAIL"
        return "PASS"

    def username_length_must_be_within_bounds(self):
        usernames = [i['username'] for i in ua_dataset[0]]
        for i in usernames:
            if not 3 < len(i) < 12:
                return "FAIL"
        return "PASS"

    def email_address_must_be_valid(self):
        return "INCOMPLETE"

    def phone_number_must_be_valid(self):
        return "INCOMPLETE"

    def authorized_date_must_be_earlier_than_authenticated_date(self):
        return "INCOMPLETE"

    def authorized_date_must_be_earlier_than_released_date(self):
        return "INCOMPLETE"

    def authenticated_date_must_be_earlier_than_released_date(self):
        return "INCOMPLETE"

    def job_title_must_exist_in_whitelist(self):
        return "INCOMPLETE"



if __name__ == "__main__":
    desc = "UserAudit - audit a dataset and optionally validate and merge user\
            input data with it."
    footer = "This program is a part of 2019's 100 Days of Coding."
    parser = argparse.ArgumentParser(description=desc, epilog=footer)
    parser.add_argument("dataset_file", action="store", help="[FILE] - load user dataset for\
                        validation.") 
    parser.add_argument("-m", "--merge",  help="[FILE] - validate \
                        and merge FILE with the user dataset.")
    parser.add_argument("--purge", action="store_true", help="purge invalid \
                        entries from dataset during audits")
    parser.add_argument("--reserved", help="[FILE] - use custom username \
                        blacklist")
    parser.add_argument("--titles", help="[FILE] - use custom job_title \
                        whitelist")
    args = parser.parse_args()
    # Does it work yet?
    if args:
        load_users_dataset(args.dataset_file)
        load_reserved_usernames()
        # TODO: Refactor this mess as a function
        ua_attrs = []
        u = UserAudits()
        for name in dir(u):
            ua_attrs.append(getattr(u, name))
        ua_funcs = filter(ismethod, ua_attrs)
        for func in ua_funcs:
            try:
                print(f"{func.__name__}: {func()}")
            except TypeError():
                pass
