# Let's take this program and make it into a command line app.
# Let's also allow the user to declare their own files for:
# - User Dataset
# - Whitelisted values
# - Blacklisted values

import json
import re
import datetime

class UserAudit():
    def load_dataset(dataset_path):
        dataset_load_flag = "r"
        if dataset_cleanup_bit:
            dataset_load_flag = "w"
        if dataset_create_bit:
            dataset_load_flag = "x"
        # TODO: Learn best error handling practices for opening files
        dataset_file = open(dataset_path, dataset_load_flag)
        # TODO: Handle errors on JSON load
        dataset = json.load(dataset_file)

    def load_list(list_path):
        list_file = open(list_path)
        loaded_list = json.load(list_file)

    # In the following functions, n is the JSON entry in an array of entries.
    # The field parameter is the name of a field in that entry.
    def empty_check(n, field):
        if not n[field]:
            return False
        return True

    # TODO: Consider allowing direct comparisons as well as substring checks

    def blacklist_check(n, field, invalid_list):
        for i in invalid_list:
            if n[field]:
                if i in n[field]:
                    return False
        return True

    def whitelist_check(n, field, whitelist):
        if not n[field]:
            return False
        if n[field] in whitelist:
            return True
        return False

    def length_check(n, field, min, max):
        if n[field]:
            if min <= len(n[field]) and len(n[field]) <= max:
                return True
        return False

    def type_check(n, field, typename):
        if not n[field]:
            return False
        if typename == "alnum":
            if not n[field].isalnum():
                return False
        if typename == "digit":
            if not n[field].isdigit():
                return False
        elif typename == "alpha":
            if not n[field].isalpha():
                return False
        return True

    def regex_check(n, field, reg):
        if not n[field]:
            return False
        if re.match(reg, n[field]) == n[field]:
            return True
        return False

    # Timestamps must be in UTC without millisecond precision
    def precedence_check(n, bef_field, aft_field):
        if not n[bef_field]:
            return False, "Before field is null."
        if not n[aft_field]:
            return False, "After field is null."
        try:
            before = datetime.datetime.strptime(
                str(n[bef_field]), "%Y-%m-%dT%H:%M:%SZ")
        except:
            return False, f"Invalid {bef_field}."
        try:
            after = datetime.datetime.strptime(
                str(n[aft_field]), "%Y-%m-%dT%H:%M:%SZ")
        except:
            return False, f"Invalid {aft_field}."
        if before < after:
            return True
        return False, f"{bef_field} is not before {aft_field}."

    def uniqueness_check(n, field, dataset):
        if n[field]:
            for entry in dataset:
                if entry["id"] != n["id"]:
                    if entry[field] == n[field]:
                        return False
            return True
        return False, f"{field} is empty."
