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


class UserAudit():
    def name_and_email_fields_required(self):
        failset = []
        for i in self.dataset[0]:
            if False in [da.empty_check(i, 'first_name'),
                        da.empty_check(i, 'last_name'),
                        da.empty_check(i, 'auth_email')]:
                failset.append(i)
        if len(failset):
            return f"FAIL: {len(failset)} items"
        return "PASS"

    def username_must_not_contain_reserved_words(self):
        failset = []
        for entry in self.dataset[0]:
            if not da.blacklist_check(entry, "username", self.username_blacklist):
                failset.append(entry)
        if len(failset):
            return f"FAIL: {len(failset)} items"
        return "PASS"

    def email_and_usernames_must_be_unique(self):
        if not da.uniqueness_check('username', self.dataset[0]):
            return "FAIL"
        if not da.uniqueness_check('auth_email', self.dataset[0]):
            return "FAIL"
        return "PASS"

    def username_length_must_be_within_bounds(self):
        for i in self.dataset[0]:
            if not da.length_check(i, 'username', 3, 12):
                return "FAIL"
        return "PASS"

    def email_address_must_be_valid(self):
        return "INCOMPLETE"

    def phone_number_must_be_valid(self):
        return "INCOMPLETE"

    def authorized_date_must_be_earlier_than_last_authenticated_date(self):
        failset = []
        for i in self.dataset[0]:
            if not da.precedence_check(i, "authorized_date",
                                       "last_authenticated_date")[0]:
                failset.append(i)
        if len(failset):
            return f"FAIL: {len(failset)} items"
        return "PASS"


    def authorized_date_must_be_earlier_than_released_date(self):
        failset = []
        for i in self.dataset[0]:
            if not da.precedence_check(i, "authorized_date",
                                       "released_date")[0]:
                failset.append(i)
        if len(failset):
            return f"FAIL: {len(failset)} items"
        return "PASS"

    def last_authenticated_date_must_be_earlier_than_released_date(self):
        failset = []
        for i in self.dataset[0]:
            if not da.precedence_check(i, "last_authenticated_date",
                                       "released_date")[0]:
                failset.append(i)
        if len(failset):
            return f"FAIL: {len(failset)} items"
        return "PASS"

    def job_title_must_exist_in_whitelist(self):
        failset = []
        for i in self.dataset[0]:
            if not da.whitelist_check(i, "job_title", self.title_whitelist):
                failset.append(i)
        if len(failset):
            return f"FAIL: {len(failset)} items"
        return "PASS"

    def report_audit_result(self):
        # Print number of entries processed, validated, purged.
        # Print information about file write actions
        return "INCOMPLETE"

    @classmethod
    def run_audit(cls, params):
        cls.dataset = da.open_dataset(params.dataset_file)
        cls.username_blacklist = da.open_list(params.reserved)
        cls.title_whitelist = da.open_list(params.titles)
        attrs = []
        u = UserAudit()
        for name in dir(u):
            attrs.append(getattr(u, name))
        funcs = filter(ismethod, attrs)
        for func in funcs:
            if func.__name__ != "run_audit":
                try:
                    print(f"{func.__name__}: {func()}")
                except TypeError():
                    pass

if __name__ == "__main__":
    desc = "UserAudit - audit a dataset and optionally validate and merge user\
            input data with it."
    footer = "This program is a part of 2019's 100 Days of Coding."
    parser = argparse.ArgumentParser(description=desc, epilog=footer)
    parser.add_argument("dataset_file", action="store", help="[FILE] - load user dataset for\
                        validation.")
    parser.add_argument("-m", "--merge", action="store_true", help="[FILE] - validate \
                        and merge FILE with the user dataset.")
    parser.add_argument("--purge", action="store_true", help="purge invalid \
                        entries from dataset during audits")
    parser.add_argument("--reserved", action="store", help="[FILE] - use custom username \
                        blacklist", default='./reserved_usernames.json')
    parser.add_argument("--titles", action="store", help="[FILE] - use custom job_title \
                        whitelist", default='./valid_user_titles.json')
    args = parser.parse_args()
    # Does it work yet?
    if args:
        UserAudit.run_audit(args)
