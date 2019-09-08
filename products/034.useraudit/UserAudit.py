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
import datetime
import json

class UserAudit():
    def name_and_email_fields_required(self):
        failset = []
        for i in self.dataset[0]:
            if False in [da.empty_check(i, 'first_name'),
                        da.empty_check(i, 'last_name'),
                        da.empty_check(i, 'auth_email')]:
                failset.append(i)
        return self.process_audit_result(failset)

    def username_must_not_contain_reserved_words(self):
        failset = []
        for i in self.dataset[0]:
            if not da.blacklist_check(i, "username", self.username_blacklist[0]):
                failset.append(i)
        return self.process_audit_result(failset)

    def email_and_usernames_must_be_unique(self):
        failset = []
        for i in self.dataset[0]:
            if not da.uniqueness_check(i, 'username', self.dataset[0]) or not da.uniqueness_check(i, 'auth_email', self.dataset[0]):
                failset.append(i)
        return self.process_audit_result(failset)

    def username_length_must_be_within_bounds(self):
        failset = []
        for i in self.dataset[0]:
            if not da.minimum_length_check(i, 'username', 3) or not da.maximum_length_check(i,  'username', 12):
                failset.append(i)
        return self.process_audit_result(failset)

    def email_address_must_be_valid(self):
        pattern = r"^\S+@\S+$"
        failset = []
        for i in self.dataset[0]:
            if not da.regex_check(i, "auth_email", pattern):
                failset.append(i)
        return self.process_audit_result(failset)

    def phone_number_must_be_valid(self):
        pattern =\
        r"^(?:\+?1[-.●]?)?\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$"
        failset = []
        for i in self.dataset[0]:
            if not da.regex_check(i, "auth_phone", pattern):
                failset.append(i)
        return self.process_audit_result(failset)

    def authorized_date_must_be_earlier_than_last_authenticated_date(self):
        failset = []
        for i in self.dataset[0]:
            if not da.precedence_check(i, "authorized_date",
                                       "last_authenticated_date")[0]:
                failset.append(i)
        return self.process_audit_result(failset)


    def authorized_date_must_be_earlier_than_released_date(self):
        failset = []
        for i in self.dataset[0]:
            if not da.precedence_check(i, "authorized_date",
                                       "released_date")[0]:
                failset.append(i)
        return self.process_audit_result(failset)

    def last_authenticated_date_must_be_earlier_than_released_date(self):
        failset = []
        for i in self.dataset[0]:
            if not da.precedence_check(i, "last_authenticated_date",
                                       "released_date")[0]:
                failset.append(i)
        return self.process_audit_result(failset)

    def job_title_must_exist_in_whitelist(self):
        failset = []
        for i in self.dataset[0]:
            if not da.whitelist_check(i, "job_title", self.title_whitelist[0]):
                failset.append(i)
        return self.process_audit_result(failset)

    @classmethod
    def process_audit_result(cls, failset):
        if len(failset):
            for i in failset:
                if i not in cls.purged_entries[0]:
                   cls.purged_entries[0].append(i)
                if i in cls.dataset[0]:
                    cls.dataset[0].pop(cls.dataset[0].index(i))
            return f"FAIL: {len(failset)} items."
        return "PASS"

    @classmethod
    def report_audit_result(cls):
        json.dump(cls.dataset[0], cls.output[1])
        json.dump(cls.purged_entries[0], cls.purged_entries[1])
        print(f"Processed {cls.dataset_initial_length} entries from {cls.dataset[1].name}, {len(cls.dataset[0])} of which were valid.")
        print(f"{len(cls.dataset[0])} validated entries were written to: {cls.output[1].name}.")
        print(f"{len(cls.purged_entries[0])} invalid files were written to: {cls.purged_entries[1].name}.")

    @classmethod
    def run_audit(cls, params):
        cls.dataset = da.open_dataset(params.dataset_file)
        cls.dataset_initial_length = len(cls.dataset[0])
        cls.output = da.open_dataset(params.output, True)
        if params.merge:
            cls.do_merge = True
            cls.inputs = da.open_dataset(params.merge)
        if params.purge:
            cls.do_purge = True
            cls.purged_entries =\
            da.open_dataset(params.purge, True)
        cls.username_blacklist = da.open_list(params.reserved)
        cls.title_whitelist = da.open_list(params.titles)
        attrs = []
        u = UserAudit()
        for name in dir(u):
            attrs.append(getattr(u, name))
        funcs = filter(ismethod, attrs)
        for func in funcs:
            if func.__name__ not in ["report_audit_result", "run_audit",
                                     "process_audit_result",
                                     "report_audit_result"]:
                try:
                    print(f"{func.__name__}: {func()}")
                except TypeError():
                    pass
        cls.report_audit_result()

if __name__ == "__main__":
    desc = "UserAudit - audit a dataset and optionally validate and merge user \
            input data with it."
    footer = "This program is a part of 2019's 100 Days of Coding."
    timestamp = datetime.datetime.utcnow().replace(microsecond=0).strftime("%Y-%m-%dT%H%M%S")
    parser = argparse.ArgumentParser(description=desc, epilog=footer)
    parser.add_argument("dataset_file", help="[FILE] - input file (dataset to \
                        be validated).")
    parser.add_argument("-m", "--merge", help="[FILE] - validate \
                        and merge FILE with the user dataset.")
    parser.add_argument("-o", "--output", default=f'./validated.{timestamp}.json',
                        help="[FILE] - destination file for validated entries.")
    parser.add_argument("-p", "--purge", default=f'./purgefile.{timestamp}.json',
                        help="[FILE] - purge invalid \
                        entries from dataset and into a separate file.")
    parser.add_argument("--reserved", help="[FILE] - use custom username \
                        blacklist", default='./reserved_usernames.json')
    parser.add_argument("--titles", help="[FILE] - use custom job_title \
                        whitelist", default='./valid_user_titles.json')
    args = parser.parse_args()
    # Does it work yet?
    if args:
        UserAudit.run_audit(args)
