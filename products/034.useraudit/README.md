UserAudit is a CLI app which validates a user dataset and optionally validates and merges user input data with it.
The validations performed are arbitrary and are used as a demonstration of the DataAudit module's generalized auditing capability.

`Usage: UserAudit.py [FILE] [OPTIONS]`

Audits the provided user dataset FILE and reports its validity.

Optionally, when the program is executed with the `-m` or `--merge` arguments (and the required file argument), audits are conducted on both files before an attempt is made to merge the provided user input data with the existing dataset. The net result of each file's audits and the merget attempt are then reported to the user.

The user may declare the following optional arguments:
```
--reserved [filename] | use provided username blacklist (JSON)
--titles [filename]   | use provided job title whitelist (JSON)
--merge [filename]    | attempt to merge provided JSON file with dataset
--purge               | remove invalid entries as they are encountered
-v                    | increase output verbosity
```

This application includes a set of configuration files, which are used by default:
- reserved_usernames.json: JSON array representing example blacklist
- valid_user_titles.json: JSON array representing example whitelist

