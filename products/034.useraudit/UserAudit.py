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


def load_users_dataset(file):
    global ua_dataset
    ua_dataset = da.open_dataset(file)

def load_reserved_usernames(file):
    global ua_username_blacklist
    ua_username_blacklist = da.open_list(file)

def load_valid_job_titles(file):
    global ua_title_whitelist
    ua_title_whitelist = da.open_list(file)

def name_and_email_fields_required(dataset):
    failset = []
    for i in dataset:
        if None in [i['first_name'], i['last_name'], i['auth_email']]:
            failset.append(i)
    if len(failset):
        return False, failset
    return True

def username_must_not_contain_reserved_words(entry):
    return

def email_and_usernames_must_be_unique(dataset, entry):
    return

def username_length_must_be_within_bounds(entry):
    return

def email_address_must_be_valid(entry):
    return

def phone_number_must_be_valid(entry):
    return

def authorized_date_must_be_earlier_than_authenticated_date(entry):
    return

def authorized_date_must_be_earlier_than_released_date(entry):
    return

def authenticated_date_must_be_earlier_than_released_date(entry):
    return

def job_title_must_exist_in_whitelist(entry):
    return



if __name__ == "__main__":
    desc = "UserAudit - audit a dataset and optionally validate and merge user\
            input data with it."
    footer = "This program is a part of 2019's 100 Days of Coding."
    parser = argparse.ArgumentParser(description=desc, epilog=footer)
    # TODO: get file argument as constant
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
        print(name_and_email_fields_required(ua_dataset[0]))
