#!/usr/bin/python3

# This command line program will import the DataAudit module and perform a
# prescribed set of audits on an existing dataset. If the path and filename of
# the dataset are not declared, the default path and file name are used. If the
# selected path and filename cannot be found, Create and open a file at the
# selected path.

import DataAudit as da
import argparse

if __name__ == "__main__":
    desc = "UserAudit - audits or creates a user dataset file."
    footer = "This program is a part of 2019's 100 Days of Coding."
    parser = argparse.ArgumentParser(description=desc, epilog=footer)
    parser.add_argument("--new", action="store_true", help="creates a new \
                        dataset file")
    parser.add_argument("dataset_file", nargs='?',
                        default='./user_input_data.json')
    args = parser.parse_args()
    # Does it work yet?
    if args:
        print(args.dataset_file)
