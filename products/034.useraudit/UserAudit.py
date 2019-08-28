#!/usr/bin/python3

# This command line program will import the DataAudit module and perform a
# prescribed set of audits on an existing dataset. If the path and filename of
# the dataset are not declared, the default path and file name are used. If the
# selected path and filename cannot be found, Create and open a file at the
# selected path.

# CONFIG FILES
# The blacklist, whitelist, and pattern matches are determined by the contents
# of their related files and will not be used in command line arguments.

# POSITIONAL ARGUMENTS
# The dataset file has a default path and filename, but the user may declare
# their own path and file name for this argument. It is the only positional
# argument in the application.

# OPTIONAL ARGUMENTS
# The following two arguments are mutually exclusive:
# new - explicitly create a new file with the selected path
# purge - invalid entries are purged during audit


import DataAudit as da
import argparse




if __name__ == "__main__":
    desc = "UserAudit - audits or creates a user dataset file."
    footer = "This program is a part of 2019's 100 Days of Coding."
    parser = argparse.ArgumentParser(description=desc, epilog=footer)
    parser.add_argument("--new", action="store_true", help="creates a new \
                        dataset file")
    # TODO: This argument is mutually exclusive with the above. Research method to
    # implement this behavior.
    parser.add_argument("--purge", action="store_true", help="purges invalid \
                        entries from dataset during audit")
    parser.add_argument("dataset_file", nargs='?',
                        default='./user_input_data.json')
    args = parser.parse_args()
    # Does it work yet?
    if args:
        chz = da.DataAudit.open_dataset(args.dataset_file)
        print(chz[0])
        print(type(chz[1]))
        print(args.dataset_file)
